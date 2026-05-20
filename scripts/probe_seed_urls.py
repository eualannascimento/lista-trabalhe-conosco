#!/usr/bin/env python3
"""Verifica URLs em seeds YAML e gera ready_to_add.csv."""

import csv
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.discover_career_urls import detect_platform, _slug_matches_url
from scripts.scoring_utils import normalize_name
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

READY = ROOT / "artifacts/ready_to_add.csv"
LIST = ROOT / "src/data/input/list.csv"
SEEDS = ROOT / "data/seeds"


def load_companies():
    rows = []
    for path in sorted(SEEDS.glob("*.yaml")):
        if path.name in ("scoring.yaml",):
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        items = data.get("companies", data.get("aliases", []))
        for c in items:
            if c.get("urls"):
                rows.append(
                    (
                        c["name"],
                        c.get("macro", "Serviços e Outros"),
                        list(c["urls"]),
                    )
                )
    return rows


def main():
    existing_names = set()
    existing_urls = set()
    with open(LIST, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            existing_names.add(normalize_name(row["Nome da Empresa"]))
            existing_urls.add(clean_url(row["URL"]))

    session = create_shared_session()
    ready = []
    companies = load_companies()
    print(f"Probing {len(companies)} seed companies with URLs...")

    def probe(item):
        name, macro, urls = item
        if normalize_name(name) in existing_names:
            return None
        for url in urls:
            url = clean_url(url)
            if url in existing_urls:
                return None
            if verify_website_status(session, url)["status"] != "1":
                continue
            if not verify_portal_has_jobs(url, session):
                continue
            if ".gupy.io" in url.lower() and not _slug_matches_url(name, url):
                continue
            return {
                "Nome da Empresa": name,
                "Segmento da Empresa": macro,
                "Plataforma": detect_platform(url),
                "URL": url,
                "evidencia": "seed_probe+strong",
            }
        return None

    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = [pool.submit(probe, c) for c in companies]
        for fut in as_completed(futs):
            res = fut.result()
            if res:
                ready.append(res)
                existing_urls.add(clean_url(res["URL"]))
                print(f"+ {res['Nome da Empresa']} -> {res['URL']}")

    if ready:
        with open(READY, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(
                f,
                fieldnames=[
                    "Nome da Empresa",
                    "Segmento da Empresa",
                    "Plataforma",
                    "URL",
                    "evidencia",
                ],
            )
            w.writeheader()
            w.writerows(ready)

    print(f"Ready: {len(ready)} -> {READY}")


if __name__ == "__main__":
    main()
