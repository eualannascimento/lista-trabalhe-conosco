#!/usr/bin/env python3
"""Move empresas de list.csv para archived.csv."""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST_CSV = ROOT / "src/data/input/list.csv"
ARCHIVED_CSV = ROOT / "src/data/input/archived.csv"

ARCHIVE_FIELDS = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
    "Data de Publicação",
    "Data de Arquivamento",
    "Motivo",
    "Issue_original",
]


def load_archived() -> list[dict]:
    if not ARCHIVED_CSV.exists():
        return []
    with open(ARCHIVED_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_archived(rows: list[dict]) -> None:
    ARCHIVED_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(ARCHIVED_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ARCHIVE_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def archive_by_status_zero(motivo: str = "sem_url_valida_pos_reparo") -> tuple[int, int]:
    today = date.today().strftime("%Y-%m-%d")
    with open(LIST_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        active = list(reader)

    archived = load_archived()
    to_archive = [r for r in active if r["Status da URL"] == "0"]
    remaining = [r for r in active if r["Status da URL"] != "0"]

    for row in to_archive:
        archived.append(
            {
                **row,
                "Data de Arquivamento": today,
                "Motivo": motivo,
                "Issue_original": row.get("Issue_original", "HTTP 404"),
            }
        )

    with open(LIST_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(remaining)

    save_archived(archived)
    return len(to_archive), len(remaining)


def archive_by_names(names: list[str], motivo: str) -> int:
    today = date.today().strftime("%Y-%m-%d")
    names_set = set(names)
    with open(LIST_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        active = list(reader)

    archived = load_archived()
    count = 0
    remaining = []
    for row in active:
        if row["Nome da Empresa"] in names_set:
            archived.append(
                {
                    **row,
                    "Data de Arquivamento": today,
                    "Motivo": motivo,
                    "Issue_original": "",
                }
            )
            count += 1
        else:
            remaining.append(row)

    with open(LIST_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(remaining)

    save_archived(archived)
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--status-zero",
        action="store_true",
        help="Arquiva todas as linhas com Status da URL = 0",
    )
    parser.add_argument("--names", nargs="*", help="Nomes exatos de empresas")
    parser.add_argument("--motivo", default="sem_url_valida_pos_reparo")
    args = parser.parse_args()

    if args.status_zero:
        n_archived, n_remaining = archive_by_status_zero(args.motivo)
        print(f"Arquivadas: {n_archived} | Restantes na lista: {n_remaining}")
        return 0

    if args.names:
        n = archive_by_names(args.names, args.motivo)
        print(f"Arquivadas: {n}")
        return 0

    print("Use --status-zero ou --names", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
