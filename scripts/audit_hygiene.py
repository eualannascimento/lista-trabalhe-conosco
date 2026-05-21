#!/usr/bin/env python3
"""Identifica entradas na lista abaixo do critério de empresa grande."""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.scoring_utils import load_scoring_config, normalize_name, should_exclude_name

LIST = ROOT / "src/data/input/list.csv"
OUT = ROOT / "artifacts/review_remove.csv"

SMALL_PATTERNS = [
    r"^2com",
    r"^3corp",
    r"^3cserv",
    r"^4mk$",
    r"^77sol",
    r"^abaco$",
    r"^abakids",
    r"^a3consult",
    r"^analytics",
    r"^wordpress-proxy",
    r"^docs\.inhire",
    r"^new\.inhire",
    r"^novo\.inhire",
    r"^inkrypton",
    r"^passbolt\.inhire",
    r"^gerador\.inhire",
    r"^carreira\.inhire",
]


def is_likely_small(name: str, config: dict) -> tuple[bool, str]:
    if should_exclude_name(name, config):
        return True, "exclude_pattern"
    n = normalize_name(name)
    for pat in SMALL_PATTERNS:
        if re.search(pat, n):
            return True, f"pattern:{pat}"
    if len(name) <= 4 and name.isupper():
        return True, "short_name"
    return False, ""


def main():
    config = load_scoring_config()
    review = []
    with open(LIST, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            flag, reason = is_likely_small(row["Nome da Empresa"], config)
            if flag:
                review.append(
                    {
                        "Nome da Empresa": row["Nome da Empresa"],
                        "URL": row["URL"],
                        "Plataforma": row["Plataforma"],
                        "Segmento da Empresa": row["Segmento da Empresa"],
                        "motivo": reason,
                        "acao_sugerida": "remover_ou_revalidar",
                    }
                )

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        if review:
            w = csv.DictWriter(f, fieldnames=list(review[0].keys()))
            w.writeheader()
            w.writerows(review)

    print(f"Review list: {len(review)} entries -> {OUT}")


if __name__ == "__main__":
    main()
