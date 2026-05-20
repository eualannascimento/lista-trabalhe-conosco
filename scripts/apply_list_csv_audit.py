#!/usr/bin/env python3
"""Apply audit fixes to src/data/input/list.csv (same columns, no schema change)."""

import csv

PATH = "src/data/input/list.csv"
FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
    "Data de Publicação",
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

SEGMENT_OVERRIDES = {
    "Votorantim Cimentos": "Indústria",
    "Red House International School": "Educação",
    "Marriott International": "Hospitalidade",
}

A_CLASSIFICAR_SEGMENTS = {
    "77sol": "Tecnologia",
    "3cservices": "Consultoria",
    "Abakids": "Educação",
    "3corptechnology": "Consultoria",
    "Abaco": "Consultoria",
    "2comconsulting": "Consultoria",
    "A3consultoria": "Consultoria",
    "3coracoes": "Alimentos e Bebidas",
    "4mk": "Tecnologia",
    "Aacd": "Saúde",
    "Analytics": "Tecnologia",
    "Analytics-ss": "Tecnologia",
    "Carreira": "Tecnologia",
    "Docs": "Tecnologia",
    "Gerador": "Tecnologia",
    "Inkrypton": "Tecnologia",
    "New": "Tecnologia",
    "Novo": "Tecnologia",
    "Passbolt": "Tecnologia",
    "Wordpress-proxy": "Tecnologia",
}

STALE_PUB_DATE = "2023-11-11"
INVALID_PUB_DATES = {"2910-09-23", "0000-00-00"}


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
    row["URL"] = clean_url(row["URL"])
    row["Plataforma"] = normalize_platform(row["URL"], row["Plataforma"])

    pub = (row.get("Data de Publicação") or "").strip()
    if pub in INVALID_PUB_DATES:
        row["Data de Publicação"] = ""

    if pub == STALE_PUB_DATE and row["Plataforma"] == "Gupy":
        row["Data de Publicação"] = ""

    name = row["Nome da Empresa"]
    if name in SEGMENT_OVERRIDES:
        row["Segmento da Empresa"] = SEGMENT_OVERRIDES[name]
    elif row["Segmento da Empresa"] == "A Classificar" and name in A_CLASSIFICAR_SEGMENTS:
        row["Segmento da Empresa"] = A_CLASSIFICAR_SEGMENTS[name]

    return row


def apply_p0(row: dict) -> dict:
    if row["Nome da Empresa"] == "Mart Minas" and (row.get("Data de Publicação") or "").strip() in INVALID_PUB_DATES:
        row["Data de Publicação"] = ""
    if row["Nome da Empresa"] == "Magazine Luiza":
        row["Data de Publicação"] = ""
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
        row = apply_p0(normalize_row(row))
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
