#!/usr/bin/env python3
"""Descobre URLs para empresas ainda ausentes de YAML, list.csv e patch."""

from __future__ import annotations

import csv
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.discover_career_urls import load_cache, save_cache
from scripts.expand_known_career_urls import CURATED_URLS, discover_with_curated
from scripts.expand_large_companies_br import COMPANIES
from scripts.scoring_utils import normalize_name
from src.py.functions.website_verification import create_shared_session

OUT = ROOT / "artifacts/discovered_remaining.json"


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
        import re

        for m in re.finditer(r"- name: (.+)", patch.read_text(encoding="utf-8")):
            names.add(normalize_name(m.group(1)))
    return names


def load_candidates(excluded: set[str]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    out: list[tuple[str, str]] = []

    for name, macro in COMPANIES:
        key = normalize_name(name)
        if not key or key in seen or key in excluded:
            continue
        seen.add(key)
        out.append((name, macro))

    scored = ROOT / "artifacts/candidates_scored.csv"
    if scored.exists():
        with open(scored, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                name = row["Nome da Empresa"]
                macro = row["Segmento da Empresa"]
                key = normalize_name(name)
                if not key or key in seen or key in excluded:
                    continue
                seen.add(key)
                out.append((name, macro))

    for name in CURATED_URLS:
        key = normalize_name(name)
        if not key or key in seen or key in excluded:
            continue
        seen.add(key)
        macro = "Serviços e Outros"
        for n, m in COMPANIES:
            if normalize_name(n) == key:
                macro = m
                break
        out.append((name, macro))

    return out


def main() -> None:
    excluded = load_excluded()
    candidates = load_candidates(excluded)
    print(f"Candidatos: {len(candidates)}")

    cache = load_cache()
    session = create_shared_session()
    found: list[dict] = []
    done = 0

    def work(item: tuple[str, str]) -> dict | None:
        return discover_with_curated(item[0], item[1], session, cache)

    with ThreadPoolExecutor(max_workers=20) as ex:
        futs = {ex.submit(work, c): c for c in candidates}
        for fut in as_completed(futs):
            done += 1
            res = fut.result()
            if res:
                found.append(res)
                print(f"+ [{len(found)}] {res['name']} -> {res['urls'][0]}")
            if done % 100 == 0:
                print(f"  {done}/{len(candidates)} found={len(found)}")
                save_cache(cache)

    save_cache(cache)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(found, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"DONE: {len(found)} -> {OUT}")


if __name__ == "__main__":
    main()
