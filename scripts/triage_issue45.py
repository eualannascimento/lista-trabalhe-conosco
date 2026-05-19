#!/usr/bin/env python3
"""Cruza issue45_report.csv com list.csv e gera issue45_triage.csv."""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUE_REPORT = ROOT / "src/data/input/issue45_report.csv"
LIST_CSV = ROOT / "src/data/input/list.csv"
TRIAGE_OUT = ROOT / "src/data/output/issue45_triage.csv"


def classify_action(issue_status: str, issue_text: str, url: str, in_list: bool, list_status: str) -> str:
    issue_text = issue_text or ""
    issue_status = (issue_status or "").strip()

    if issue_status == "200" and "Type Mismatch" in issue_text:
        return "ignorar"
    if any(
        p in url
        for p in (
            "wday/cxs/",
            "boards-api.greenhouse.io",
            "eightfold.ai/api",
            "apply.workable.com/api",
        )
    ):
        return "ignorar"
    if not in_list:
        return "ignorar"
    if list_status == "1" and issue_status == "200":
        return "ignorar"
    if list_status == "0" or issue_status in ("404", "400", "403", "526", "202") or issue_status == "Error":
        if "Type Mismatch" in issue_text:
            return "ignorar"
        return "corrigir"
    return "ignorar"


def load_list_by_url() -> dict[str, dict]:
    by_url = {}
    with open(LIST_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            by_url[row["URL"].strip()] = row
    return by_url


def main() -> int:
    if not ISSUE_REPORT.exists():
        print(f"Arquivo não encontrado: {ISSUE_REPORT}", file=sys.stderr)
        return 1

    list_by_url = load_list_by_url()
    TRIAGE_OUT.parent.mkdir(parents=True, exist_ok=True)

    counts = {"corrigir": 0, "ignorar": 0, "arquivar": 0}
    rows_out = []

    with open(ISSUE_REPORT, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row["URL"].strip()
            list_row = list_by_url.get(url)
            in_list = list_row is not None
            list_status = list_row["Status da URL"] if list_row else ""
            nome = list_row["Nome da Empresa"] if list_row else ""
            acao = classify_action(
                row.get("Status", ""),
                row.get("Issue", ""),
                url,
                in_list,
                list_status,
            )
            counts[acao] = counts.get(acao, 0) + 1
            rows_out.append(
                {
                    "Nome da Empresa": nome,
                    "URL": url,
                    "Platform_issue": row.get("Platform", ""),
                    "Status_issue": row.get("Status", ""),
                    "Issue": row.get("Issue", ""),
                    "Status_lista": list_status,
                    "acao": acao,
                }
            )

    # Entradas na lista com Status=0 que não estão no report
    report_urls = {r["URL"] for r in rows_out}
    for url, list_row in list_by_url.items():
        if list_row["Status da URL"] == "0" and url not in report_urls:
            rows_out.append(
                {
                    "Nome da Empresa": list_row["Nome da Empresa"],
                    "URL": url,
                    "Platform_issue": list_row.get("Plataforma", ""),
                    "Status_issue": "",
                    "Issue": "Status 0 no list.csv",
                    "Status_lista": "0",
                    "acao": "corrigir",
                }
            )
            counts["corrigir"] += 1

    fieldnames = [
        "Nome da Empresa",
        "URL",
        "Platform_issue",
        "Status_issue",
        "Issue",
        "Status_lista",
        "acao",
    ]
    with open(TRIAGE_OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(rows_out, key=lambda x: (x["acao"], x["Nome da Empresa"])))

    print(f"Triage salvo em {TRIAGE_OUT}")
    print(f"Resumo: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
