#!/usr/bin/env python3
"""Ingere artifacts/ready_to_add.csv via new_items.csv + fluxo do main.py."""

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.py.functions.df_operations import clean_url

READY = ROOT / "artifacts/ready_to_add.csv"
NEW_ITEMS = ROOT / "src/data/input/new_items.csv"
LIST = ROOT / "src/data/input/list.csv"

NEW_FIELDS = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]


def main():
    with open(READY, newline="", encoding="utf-8") as f:
        incoming = list(csv.DictReader(f))
    if not incoming:
        print("No ready_to_add rows")
        return

    with open(LIST, newline="", encoding="utf-8") as f:
        existing_urls = {clean_url(r["URL"]) for r in csv.DictReader(f)}

    batch = []
    for item in incoming:
        url = clean_url(item["URL"])
        if url in existing_urls:
            continue
        batch.append(
            {
                "Nome da Empresa": item["Nome da Empresa"].strip(),
                "Segmento da Empresa": item["Segmento da Empresa"],
                "Plataforma": item["Plataforma"],
                "URL": url,
            }
        )

    if not batch:
        print("No new rows to ingest (all URLs already in list)")
        return

    with open(NEW_ITEMS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=NEW_FIELDS)
        w.writeheader()
        w.writerows(batch)

    print(f"Wrote {len(batch)} rows to {NEW_ITEMS}")
    result = subprocess.run(
        [sys.executable, str(ROOT / "main.py")],
        cwd=str(ROOT),
        check=False,
    )
    if result.returncode != 0:
        sys.exit(result.returncode)

    with open(LIST, newline="", encoding="utf-8") as f:
        total = sum(1 for _ in csv.DictReader(f))
    print(f"List total after ingest: {total}")


if __name__ == "__main__":
    main()
