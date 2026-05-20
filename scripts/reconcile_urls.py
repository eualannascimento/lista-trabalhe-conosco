#!/usr/bin/env python3
"""Revalida URLs do list.csv, tenta corrigir inativas e gera relatório."""

import csv
import importlib.util
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.segment_macro_map import to_macro
from src.py.functions.df_operations import clean_url
from src.py.functions.website_verification import (
    create_shared_session,
    verify_website_status,
)

_guesser_path = os.path.join(os.path.dirname(__file__), "fix_vagas_urls_guesser.py")
_spec = importlib.util.spec_from_file_location("fix_vagas_urls_guesser", _guesser_path)
_guesser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_guesser)
is_valid_ats = _guesser.is_valid_ats

LIST_PATH = os.path.join(ROOT, "src/data/input/list.csv")
REPORT_PATH = os.path.join(ROOT, "artifacts/url_reconcile_report.csv")
FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
]

MAX_WORKERS = 12
FIX_INACTIVE = os.environ.get("FIX_INACTIVE", "1") == "1"


def normalize_platform(url: str, platform: str) -> str:
    u = url.lower()
    if ".gupy.io" in u or "carreiras.gupy.io/" in u:
        return "Gupy"
    if platform == "Inhire":
        return "InHire"
    return platform


def load_rows():
    with open(LIST_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row.pop("Data de Publicação", None)
    return rows


def save_rows(rows):
    with open(LIST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def verify_row(session, row):
    url = clean_url(row["URL"])
    result = verify_website_status(session, url)
    return url, result


def try_fix_url(company_name: str, current_url: str) -> str | None:
    found = is_valid_ats(company_name)
    if not found:
        return None
    found = clean_url(found)
    if found == clean_url(current_url):
        return None
    session = create_shared_session()
    check = verify_website_status(session, found)
    if check["status"] == "1":
        return found
    return None


def main():
    os.makedirs(os.path.join(ROOT, "artifacts"), exist_ok=True)
    rows = load_rows()
    for row in rows:
        row["URL"] = clean_url(row["URL"])
        row["Plataforma"] = normalize_platform(row["URL"], row.get("Plataforma", ""))
        row["Segmento da Empresa"] = to_macro(
            row.get("Segmento da Empresa", ""), row.get("Nome da Empresa", "")
        )

    session = create_shared_session()
    report = []
    fixed = 0
    verified_ok = 0

    print(f"Verificando {len(rows)} URLs...")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(verify_row, session, row): row for row in rows}
        done = 0
        for future in as_completed(futures):
            row = futures[future]
            done += 1
            old_status = row.get("Status da URL", "0")
            old_url = row["URL"]
            try:
                url, result = future.result()
            except Exception as e:
                result = {"status": "0", "error": str(e)}
                url = old_url

            new_status = result["status"]
            new_url = url
            action = "verified"

            if new_status == "0" and FIX_INACTIVE:
                candidate = try_fix_url(row["Nome da Empresa"], old_url)
                if candidate:
                    new_url = candidate
                    new_status = "1"
                    row["Plataforma"] = normalize_platform(new_url, row["Plataforma"])
                    action = "fixed_url"
                    fixed += 1

            row["URL"] = new_url
            row["Status da URL"] = new_status
            if new_status == "1":
                verified_ok += 1

            report.append(
                {
                    "Nome da Empresa": row["Nome da Empresa"],
                    "URL_antiga": old_url,
                    "URL_nova": new_url,
                    "Status_antigo": old_status,
                    "Status_novo": new_status,
                    "Acao": action,
                    "Erro": result.get("error") or "",
                }
            )
            if done % 100 == 0 or done == len(rows):
                print(f"  {done}/{len(rows)} | ok={verified_ok} | fixed={fixed}")

    with open(REPORT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(report[0].keys()))
        writer.writeheader()
        writer.writerows(report)

    save_rows(rows)
    inactive = sum(1 for r in rows if r["Status da URL"] == "0")
    print(
        f"Salvo {LIST_PATH}: {len(rows)} linhas, {verified_ok} ativas, "
        f"{inactive} inativas, {fixed} URLs corrigidas"
    )
    print(f"Relatório: {REPORT_PATH}")


if __name__ == "__main__":
    main()
