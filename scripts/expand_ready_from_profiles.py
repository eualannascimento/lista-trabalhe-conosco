#!/usr/bin/env python3
"""Gera/atualiza ready_to_add.csv a partir de URLs curadas (perfil da lista)."""

import csv
import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.add_verified_companies import CANDIDATES as VERIFIED_CANDIDATES
from scripts.segment_macro_map import to_macro
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

_fix_path = ROOT / "scripts/fix_inactive_and_expand.py"
_spec = importlib.util.spec_from_file_location("fix_inactive", _fix_path)
_fix = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_fix)

READY = ROOT / "artifacts/ready_to_add.csv"
LIST = ROOT / "src/data/input/list.csv"


def detect_platform(url: str) -> str:
    u = url.lower()
    if ".gupy.io" in u or "carreiras.gupy.io" in u:
        return "Gupy"
    if "greenhouse.io" in u:
        return "Greenhouse"
    if "inhire" in u:
        return "InHire"
    if "lever.co" in u:
        return "Lever"
    if "workday" in u or "myworkdayjobs" in u:
        return "Workday"
    if "successfactors" in u or "sapsf" in u:
        return "SAP SuccessFactors"
    if "infojobs" in u or "pandape" in u:
        return "InfoJobs"
    if "izirh" in u:
        return "IziRH"
    if "recrut.ai" in u:
        return "Recrut.ai"
    return "Site da Empresa"


def load_existing():
    names = set()
    urls = set()
    with open(LIST, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(row["Nome da Empresa"].strip().lower())
            urls.add(clean_url(row["URL"]))
    return names, urls


def curated_rows():
    rows = []
    for name, macro, urls in _fix.NEW_BY_PROFILE:
        rows.append((name, macro, urls))
    for name, segment, _plat, urls in VERIFIED_CANDIDATES:
        rows.append((name, to_macro(segment, name), urls))
    return rows


def main():
    os.makedirs(ROOT / "artifacts", exist_ok=True)
    existing_names, existing_urls = load_existing()
    session = create_shared_session()
    ready = []

    if READY.exists():
        with open(READY, newline="", encoding="utf-8") as f:
            ready = list(csv.DictReader(f))

    ready_urls = {clean_url(r["URL"]) for r in ready}
    ready_names = {r["Nome da Empresa"].strip().lower() for r in ready}

    added = 0
    for name, macro, urls in curated_rows():
        key = name.strip().lower()
        if key in existing_names or key in ready_names:
            continue
        for url in urls:
            url = clean_url(url)
            if url in existing_urls or url in ready_urls:
                continue
            if verify_website_status(session, url)["status"] != "1":
                continue
            if not verify_portal_has_jobs(url, session):
                continue
            ready.append(
                {
                    "Nome da Empresa": name,
                    "Segmento da Empresa": macro,
                    "Plataforma": detect_platform(url),
                    "URL": url,
                    "evidencia": "curated_profile+strong",
                }
            )
            ready_urls.add(url)
            ready_names.add(key)
            added += 1
            print(f"+ {name} -> {url}")
            break

    fields = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL", "evidencia"]
    with open(READY, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(ready)

    print(f"Curated added: {added}. Total ready: {len(ready)}")


if __name__ == "__main__":
    main()
