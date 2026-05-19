#!/usr/bin/env python3
"""Repara URLs com Status=0 em list.csv usando candidatos ATS/Gupy."""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from url_repair import find_replacement_url, infer_platform  # noqa: E402

LIST_CSV = ROOT / "src/data/input/list.csv"
TRIAGE_CSV = ROOT / "src/data/output/issue45_triage.csv"

# Correções manuais confirmadas (nome exato no CSV -> nova URL)
MANUAL_FIXES = {
    "Carrefour Brasil": "https://grupocarrefourbrasil.gupy.io",
    "Odous de Deus": "https://odousdedeus.gupy.io",
}


def load_triage_corrigir() -> set[str]:
    if not TRIAGE_CSV.exists():
        return set()
    urls = set()
    with open(TRIAGE_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acao") == "corrigir":
                urls.add(row["URL"].strip())
    return urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--all-status-zero", action="store_true", help="Ignora triage e repara todo Status=0")
    args = parser.parse_args()

    corrigir_urls = load_triage_corrigir() if not args.all_status_zero else None

    with open(LIST_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    fixed = 0
    for row in rows:
        if row["Status da URL"] != "0":
            continue
        if corrigir_urls is not None and row["URL"] not in corrigir_urls:
            continue

        name = row["Nome da Empresa"]
        old_url = row["URL"]
        new_url = MANUAL_FIXES.get(name)

        if not new_url:
            new_url = find_replacement_url(name, old_url)

        if not new_url or new_url.rstrip("/") == old_url.rstrip("/"):
            continue

        print(f"FIX: {name} | {old_url} -> {new_url}")
        if not args.dry_run:
            row["URL"] = new_url
            row["Plataforma"] = infer_platform(new_url)
            row["Status da URL"] = "0"
        fixed += 1

    if not args.dry_run and fixed:
        with open(LIST_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    print(f"Total corrigidas: {fixed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
