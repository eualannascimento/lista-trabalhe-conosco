#!/usr/bin/env python3
"""
Gera issue45_report.csv a partir de list.csv e padrões da issue #45.
Inclui Status=0 (falhas HTTP) e Status=1 com padrões Type Mismatch do classifica-vagas.
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST_CSV = ROOT / "src/data/input/list.csv"
OUT = ROOT / "src/data/input/issue45_report.csv"

TYPE_MISMATCH_PATTERNS = (
    "pandape.infojobs",
    "oraclecloud.com",
    "teamtailor.com",
    "ashbyhq.com",
    "recrut.ai",
    "izirh.io",
    "quickin.io",
    "cliqx.com.br",
    "senior.com.br/hcm",
    "pepsicojobs.com",
    "izirh",
    "pandape.infojobs",
    "jobs.recrut.ai",
    "avature.net",
    "phenom",
    "kpmg.com",
    "ey.com",
    "ibm.com",
    "dell.com",
    "unilever.com",
    "pgcareers.com",
    "paramount.com",
    "crowdstrike.com",
    "cloudera.com",
    "livenationentertainment.com",
    "gehealthcare.com",
    "virtasant.teamtailor",
    "loft.teamtailor",
)

API_ONLY_PATTERNS = (
    "wday/cxs/",
    "boards-api.greenhouse.io",
    "eightfold.ai/api",
    "apply.workable.com/api",
)


def infer_issue(url: str, status: str) -> tuple[str, str]:
    if any(p in url for p in API_ONLY_PATTERNS):
        return "400", "HTTP 400"
    if status == "0":
        if "gupy.io" in url:
            return "404", "HTTP 404"
        if " " in url:
            return "Error", "Connection Error: invalid URL"
        return "404", "HTTP 404"
    if any(p in url for p in TYPE_MISMATCH_PATTERNS):
        return "200", "Type Mismatch (Expected JSON, got HTML)"
    return "", ""


def main() -> None:
    rows = []
    with open(LIST_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = row["URL"]
            list_status = row["Status da URL"]
            issue_status, issue_text = infer_issue(url, list_status)
            if not issue_status and list_status == "1":
                continue
            if not issue_status:
                issue_status, issue_text = "404", "HTTP 404"
            rows.append(
                {
                    "Platform": row["Plataforma"],
                    "URL": url,
                    "Status": issue_status,
                    "Issue": issue_text,
                    "Content-Type": "text/html; charset=utf-8" if issue_status == "200" else "",
                }
            )

    # URLs da issue #45 que não estão no list.csv (APIs do classifica-vagas)
    extra = [
        ("Workday", "https://3m.wd1.myworkdayjobs.com/wday/cxs/3m/Search/jobs", "400", "HTTP 400"),
        ("Greenhouse", "https://boards-api.greenhouse.io/v1/boards/aztec/jobs", "404", "HTTP 404"),
        ("Workday", "https://adobe.wd5.myworkdayjobs.com/wday/cxs/adobe/external_experienced/jobs", "400", "HTTP 400"),
    ]
    existing_urls = {r["URL"] for r in rows}
    for platform, url, st, issue in extra:
        if url not in existing_urls:
            rows.append(
                {
                    "Platform": platform,
                    "URL": url,
                    "Status": st,
                    "Issue": issue,
                    "Content-Type": "application/json",
                }
            )

    fieldnames = ["Platform", "URL", "Status", "Issue", "Content-Type"]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Gerado {OUT} com {len(rows)} linhas")


if __name__ == "__main__":
    main()
