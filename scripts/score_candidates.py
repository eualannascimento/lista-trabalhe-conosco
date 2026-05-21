#!/usr/bin/env python3
"""Filtra candidatos por score mínimo e remove os já presentes em list.csv."""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.scoring_utils import (
    compute_score,
    load_scoring_config,
    normalize_name,
    should_exclude_name,
)

RAW = ROOT / "artifacts/candidates_raw.csv"
OUT = ROOT / "artifacts/candidates_scored.csv"
LIST = ROOT / "src/data/input/list.csv"


def load_existing_names():
    names = set()
    with open(LIST, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(normalize_name(row["Nome da Empresa"]))
    return names


def main():
    config = load_scoring_config()
    min_score = config["min_score"]
    existing = load_existing_names()
    passed = []
    skipped = 0

    with open(RAW, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["Nome da Empresa"]
            if should_exclude_name(name, config):
                skipped += 1
                continue
            key = normalize_name(name)
            if key in existing:
                skipped += 1
                continue
            signals = {
                "b3": row["b3"] in ("True", "true", "1", True),
                "top": row["top"] in ("True", "true", "1", True),
                "revenue": row["revenue"] in ("True", "true", "1", True),
                "employees": row["employees"] in ("True", "true", "1", True),
                "fortune": row["fortune"] in ("True", "true", "1", True),
            }
            score = compute_score(signals, config)
            if score < min_score:
                skipped += 1
                continue
            passed.append(
                {
                    "Nome da Empresa": name,
                    "Segmento da Empresa": row["Segmento da Empresa"],
                    "score": score,
                    "b3": signals["b3"],
                    "top": signals["top"],
                    "source": row.get("source", ""),
                }
            )

    passed.sort(key=lambda x: (-int(x["score"]), x["Nome da Empresa"]))

    fields = ["Nome da Empresa", "Segmento da Empresa", "score", "b3", "top", "source"]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(passed)

    print(f"Scored: {len(passed)} pass (min {min_score}), skipped {skipped}")
    print(f"Output: {OUT}")


if __name__ == "__main__":
    main()
