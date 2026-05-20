#!/usr/bin/env python3
"""Apply audit fixes to src/data/input/list.csv."""

import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.segment_macro_map import to_macro

PATH = os.path.join(ROOT, "src/data/input/list.csv")
FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
]

URLS_TO_REMOVE = {
    "https://positivotecnologia.gupy.io",
    "https://hering.gupy.io",
    "https://ache.gupy.io",
    "https://job-boards.greenhouse.io/arcoeducacao",
    "https://boards.greenhouse.io/linx",
    "https://job-boards.greenhouse.io/stone",
    "https://boards.greenhouse.io/stone",
    "https://suzano.inhire.app/vagas",
    "https://vale.eightfold.ai/careers?location=Brazil",
    "https://job-boards.greenhouse.io/wildlifestudios",
}


def clean_url(url: str) -> str:
    return url.strip().rstrip("/")


def normalize_platform(url: str, platform: str) -> str:
    u = url.lower()
    if ".gupy.io" in u or "carreiras.gupy.io/" in u:
        return "Gupy"
    if platform == "Inhire":
        return "InHire"
    return platform


def normalize_row(row: dict) -> dict:
    row.pop("Data de Publicação", None)
    row["URL"] = clean_url(row["URL"])
    row["Plataforma"] = normalize_platform(row["URL"], row["Plataforma"])
    row["Segmento da Empresa"] = to_macro(
        row.get("Segmento da Empresa", ""), row.get("Nome da Empresa", "")
    )
    if row["Nome da Empresa"] == "Odous de Deus":
        row["URL"] = "https://odousdedeus.gupy.io"
        row["Plataforma"] = "Gupy"
    return row


def main():
    with open(PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out = []
    removed = 0
    for row in rows:
        row = normalize_row(row)
        if row["URL"] in URLS_TO_REMOVE:
            removed += 1
            continue
        out.append(row)

    with open(PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {len(out)} rows (removed {removed})")


if __name__ == "__main__":
    main()
