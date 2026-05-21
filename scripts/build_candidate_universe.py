#!/usr/bin/env python3
"""Gera universo bruto de candidatos a partir de seeds e YAML."""

import csv
import os
import re
import sys
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.company_seeds_data import COMPANY_SEEDS
from scripts.scoring_utils import normalize_name

OUT = ROOT / "artifacts/candidates_raw.csv"
SEEDS_DIR = ROOT / "data/seeds"

BRAPI_SECTOR_MACRO = {
    "Finance": "Financeiro",
    "Energy Minerals": "Energia e Utilities",
    "Utilities": "Energia e Utilities",
    "Technology Services": "Tecnologia",
    "Retail Trade": "Varejo e Consumo",
    "Health Technology": "Saúde",
    "Producer Manufacturing": "Indústria",
    "Transportation": "Logística e Mobilidade",
    "Consumer Non-Durables": "Varejo e Consumo",
    "Commercial Services": "Serviços e Outros",
    "Non-Energy Minerals": "Indústria",
    "Process Industries": "Indústria",
    "Consumer Durables": "Varejo e Consumo",
    "Distribution Services": "Varejo e Consumo",
    "Communications": "Energia e Utilities",
    "Industrial Services": "Indústria",
    "Health Services": "Saúde",
    "Electronic Technology": "Tecnologia",
    "Consumer Services": "Varejo e Consumo",
}


def format_brapi_name(raw: str) -> str:
    """Converte nome bruto da B3/brapi para forma legível."""
    n = (raw or "").strip()
    n = re.sub(r"\s*-\s*BRASIL.*$", "", n, flags=re.I)
    n = re.sub(r"\s*S\.?A\.?\s*$", "", n, flags=re.I)
    n = re.sub(r"\s*BOLSA.*$", "", n, flags=re.I)
    n = re.sub(r"\s*BCO\s+", "Banco ", n, flags=re.I)
    n = re.sub(r"\s*CIA\s+", "Companhia ", n, flags=re.I)
    n = re.sub(r"\s+", " ", n).strip()
    if not n:
        return raw
    return n.title() if n.isupper() else n


def load_brapi_stocks():
    """Lista de ações B3 via API pública brapi (sem token)."""
    try:
        resp = requests.get("https://brapi.dev/api/quote/list", timeout=30)
        resp.raise_for_status()
        stocks = resp.json().get("stocks", [])
    except requests.RequestException as e:
        print(f"brapi skip: {e}")
        return []

    rows = []
    seen = set()
    for s in stocks:
        if s.get("type") != "stock":
            continue
        name = format_brapi_name(s.get("name", ""))
        key = normalize_name(name)
        if not key or key in seen or len(name) < 3:
            continue
        seen.add(key)
        macro = BRAPI_SECTOR_MACRO.get(s.get("sector", ""), "Serviços e Outros")
        rows.append(
            {
                "name": name,
                "macro": macro,
                "b3": True,
                "top": False,
                "revenue": True,
                "employees": False,
                "fortune": False,
                "source": "brapi_quote_list",
            }
        )
    return rows


def load_yaml_seeds():
    rows = []
    for path in SEEDS_DIR.glob("*.yaml"):
        if path.name == "scoring.yaml":
            continue
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for c in data.get("companies", []):
            rows.append(
                {
                    "name": c["name"],
                    "macro": c.get("macro", "Serviços e Outros"),
                    "b3": c.get("b3", False),
                    "top": c.get("top", False),
                    "revenue": c.get("revenue", False),
                    "employees": c.get("employees", False),
                    "fortune": c.get("fortune", False),
                    "source": path.stem,
                }
            )
    return rows


def main():
    os.makedirs(ROOT / "artifacts", exist_ok=True)
    seen = set()
    out = []

    for name, macro, sig in COMPANY_SEEDS:
        key = normalize_name(name)
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "Nome da Empresa": name,
                "Segmento da Empresa": macro,
                "b3": sig.get("b3", False),
                "top": sig.get("top", False),
                "revenue": sig.get("revenue", False),
                "employees": sig.get("employees", False),
                "fortune": sig.get("fortune", False),
                "source": "company_seeds_data",
            }
        )

    for row in load_yaml_seeds():
        key = normalize_name(row["name"])
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "Nome da Empresa": row["name"],
                "Segmento da Empresa": row["macro"],
                "b3": row["b3"],
                "top": row["top"],
                "revenue": row["revenue"],
                "employees": row["employees"],
                "fortune": row["fortune"],
                "source": row["source"],
            }
        )

    for row in load_brapi_stocks():
        key = normalize_name(row["name"])
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "Nome da Empresa": row["name"],
                "Segmento da Empresa": row["macro"],
                "b3": row["b3"],
                "top": row["top"],
                "revenue": row["revenue"],
                "employees": row["employees"],
                "fortune": row["fortune"],
                "source": row["source"],
            }
        )

    fields = [
        "Nome da Empresa",
        "Segmento da Empresa",
        "b3",
        "top",
        "revenue",
        "employees",
        "fortune",
        "source",
    ]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)

    print(f"Wrote {len(out)} candidates to {OUT}")


if __name__ == "__main__":
    main()
