#!/usr/bin/env python3
"""Descobre URLs para empresas ausentes de YAML e list.csv."""

import csv
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from unidecode import unidecode

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.expand_large_companies_br import COMPANIES
from scripts.expand_known_career_urls import CURATED_URLS, discover_with_curated
from scripts.scoring_utils import normalize_name
from scripts.discover_career_urls import load_cache, save_cache
from src.py.functions.website_verification import create_shared_session

OUT = ROOT / "artifacts/discovered_urls.json"


def norm(name: str) -> str:
    n = unidecode((name or "").lower())
    n = re.sub(r"\s*(s/?a\.?|ltda\.?|holding)\s*", " ", n)
    n = re.sub(r"[^a-z0-9]+", "", n)
    return n.strip()


def load_existing() -> set[str]:
    import yaml

    names = set()
    with open(ROOT / "data/seeds/known_career_urls.yaml", encoding="utf-8") as f:
        for c in yaml.safe_load(f).get("companies", []):
            names.add(norm(c["name"]))
    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(norm(row["Nome da Empresa"]))
    return names


def load_candidates(existing: set[str]) -> list[tuple[str, str]]:
    seen = set()
    out = []
    for name, macro in COMPANIES:
        k = norm(name)
        if not k or k in seen or k in existing:
            continue
        seen.add(k)
        out.append((name, macro))
    return out


def main():
    existing = load_existing()
    candidates = load_candidates(existing)
    print(f"Candidatos: {len(candidates)}")

    cache = load_cache()
    session = create_shared_session()
    found = []
    done = 0

    def work(item):
        return discover_with_curated(item[0], item[1], session, cache)

    with ThreadPoolExecutor(max_workers=16) as ex:
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
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(found, f, ensure_ascii=False, indent=2)
    print(f"DONE: {len(found)} -> {OUT}")


if __name__ == "__main__":
    main()
