#!/usr/bin/env python3
"""Verifica CURATED_URLS ausentes de YAML/list.csv e gera JSON para o patch."""

from __future__ import annotations

import csv
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.expand_known_career_urls import CURATED_URLS
from scripts.expand_large_companies_br import COMPANIES
from scripts.scoring_utils import normalize_name
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

OUT = ROOT / "artifacts/curated_batch_verified.json"
BAD_FRAGMENTS = ("banco.gupy.io", "carreiras.gupy.io/", "portal.gupy.io", "vagas.gupy.io")


def load_excluded() -> set[str]:
    names: set[str] = set()
    with open(ROOT / "data/seeds/known_career_urls.yaml", encoding="utf-8") as f:
        for c in yaml.safe_load(f).get("companies", []):
            names.add(normalize_name(c["name"]))
    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(normalize_name(row["Nome da Empresa"]))
    patch = ROOT / "artifacts/known_career_urls_patch.yaml"
    if patch.exists():
        for m in re.finditer(r"- name: (.+)", patch.read_text(encoding="utf-8")):
            names.add(normalize_name(m.group(1)))
    return names


def load_csv_urls() -> set[str]:
    urls: set[str] = set()
    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            urls.add(clean_url(row["URL"]))
    return urls


def is_bad(url: str) -> bool:
    u = url.lower()
    return any(b in u for b in BAD_FRAGMENTS)


def verify_one(name: str, macro: str, urls: list[str], session) -> dict | None:
    for url in urls:
        if is_bad(url):
            continue
        url = clean_url(url)
        if verify_website_status(session, url)["status"] != "1":
            continue
        if not verify_portal_has_jobs(url, session):
            continue
        good = [url]
        for u in urls:
            u = clean_url(u)
            if u != url and not is_bad(u):
                good.append(u)
            if len(good) >= 3:
                break
        return {"name": name, "macro": macro, "urls": good[:3]}
    return None


def main() -> None:
    excluded = load_excluded()
    csv_urls = load_csv_urls()
    macro_map = {normalize_name(n): m for n, m in COMPANIES}

    candidates: list[tuple[str, str, list[str]]] = []
    for name, urls in CURATED_URLS.items():
        key = normalize_name(name)
        if key in excluded:
            continue
        primary = clean_url(urls[0])
        if primary in csv_urls:
            continue
        macro = macro_map.get(key, "Serviços e Outros")
        candidates.append((name, macro, urls))

    print(f"Verificando {len(candidates)} candidatos...")
    session = create_shared_session()
    verified: list[dict] = []

    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = {
            ex.submit(verify_one, name, macro, urls, session): name
            for name, macro, urls in candidates
        }
        for fut in as_completed(futs):
            res = fut.result()
            if res:
                verified.append(res)
                print(f"+ [{len(verified)}] {res['name']} -> {res['urls'][0]}")

    OUT.write_text(json.dumps(verified, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"DONE: {len(verified)} -> {OUT}")


if __name__ == "__main__":
    main()
