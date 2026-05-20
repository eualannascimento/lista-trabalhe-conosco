#!/usr/bin/env python3
"""Descobre URLs de carreira para candidatos aprovados com verificação forte."""

import csv
import importlib.util
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.scoring_utils import normalize_name
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

_guesser_path = ROOT / "scripts/fix_vagas_urls_guesser.py"
_spec = importlib.util.spec_from_file_location("fix_vagas_urls_guesser", _guesser_path)
_guesser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_guesser)

SCORED = ROOT / "artifacts/candidates_scored.csv"
READY = ROOT / "artifacts/ready_to_add.csv"
PENDING = ROOT / "artifacts/pending_companies.csv"
CACHE = ROOT / "artifacts/url_cache.json"
LIST = ROOT / "src/data/input/list.csv"

MAX_WORKERS = 10
LIMIT = int(os.environ.get("DISCOVER_LIMIT", "350"))


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "", name.lower())
    return s[:48]


def detect_platform(url: str) -> str:
    u = url.lower()
    if ".gupy.io" in u or "carreiras.gupy.io" in u:
        return "Gupy"
    if "greenhouse.io" in u:
        return "Greenhouse"
    if "inhire" in u:
        return "InHire"
    if "lever.co" in u:
        return "Lever"
    if "workday" in u or "myworkdayjobs" in u:
        return "Workday"
    if "successfactors" in u or "sapsf" in u:
        return "SAP SuccessFactors"
    if "infojobs" in u or "pandape" in u:
        return "InfoJobs"
    if "workable.com" in u:
        return "Workable"
    if "eightfold.ai" in u:
        return "Eightfold"
    return "Site da Empresa"


def load_cache():
    if CACHE.exists():
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    os.makedirs(CACHE.parent, exist_ok=True)
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=0)


def load_known_url_map() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for filename in ("known_career_urls.yaml", "b3_slug_aliases.yaml"):
        path = ROOT / "data/seeds" / filename
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        items = data.get("companies", data.get("aliases", []))
        for c in items:
            key = normalize_name(c["name"])
            if not key:
                continue
            urls = list(c.get("urls", []))
            out.setdefault(key, [])
            for u in urls:
                if u not in out[key]:
                    out[key].append(u)
    return out


def get_known_urls(name: str) -> list[str]:
    return load_known_url_map().get(normalize_name(name), [])


def candidate_urls(name: str) -> list[str]:
    slug = slugify(name)
    parts = name.lower().split()
    short = parts[0] if parts else slug
    urls = []
    urls.extend(get_known_urls(name))
    if len(slug) >= 5:
        urls.append(f"https://{slug}.gupy.io")
    if len(short) >= 5 and short != slug:
        urls.append(f"https://{short}.gupy.io")
    if len(slug) >= 4:
        urls.extend(
            [
                f"https://boards.greenhouse.io/{slug}",
                f"https://job-boards.greenhouse.io/{slug}",
            ]
        )
    seen = set()
    deduped = []
    for u in urls:
        u = clean_url(u)
        if u not in seen:
            seen.add(u)
            deduped.append(u)
    return deduped


def _slug_matches_url(name: str, url: str) -> bool:
    """Evita subdomínios genéricos (ex.: banco.gupy.io para Banco Amazonia)."""
    slug = slugify(name)
    host = url.lower().split("//", 1)[-1].split("/")[0].split(".")[0]
    if len(host) < 4:
        return False
    generic = {"banco", "bco", "companhia", "grupo", "empreendimentos", "terra", "mundial"}
    if host in generic and host not in slug:
        return False
    return host in slug or slug.startswith(host) or host.startswith(slug[: max(4, len(host))])


def discover_one(name: str, macro: str, session, cache: dict) -> dict:
    key = normalize_name(name)
    if key in cache:
        c = cache[key]
        if c.get("url"):
            return {**c, "Nome da Empresa": name, "Segmento da Empresa": macro}

    urls_tried = []

    found = _guesser.is_valid_ats(name)
    if found:
        found = clean_url(found)
        urls_tried.append(found)
        if (
            verify_website_status(session, found)["status"] == "1"
            and verify_portal_has_jobs(found, session)
        ):
            result = {
                "Nome da Empresa": name,
                "Segmento da Empresa": macro,
                "Plataforma": detect_platform(found),
                "URL": found,
                "evidencia": "ats_guesser+strong",
            }
            cache[key] = result
            return result

    for url in candidate_urls(name):
        url = clean_url(url)
        if url in urls_tried:
            continue
        urls_tried.append(url)
        basic = verify_website_status(session, url)
        if basic["status"] != "1":
            continue
        if not verify_portal_has_jobs(url, session):
            continue
        if ".gupy.io" in url.lower() and not _slug_matches_url(name, url):
            continue
        plat = detect_platform(url)
        result = {
            "Nome da Empresa": name,
            "Segmento da Empresa": macro,
            "Plataforma": plat,
            "URL": url,
            "evidencia": "known_or_guess+strong",
        }
        cache[key] = result
        return result

    cache[key] = {"pending": True}
    return {
        "Nome da Empresa": name,
        "Segmento da Empresa": macro,
        "pending": True,
        "motivo": "no_url_strong_verify",
    }


def load_existing_urls():
    urls = set()
    with open(LIST, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            urls.add(clean_url(row["URL"]))
    return urls


def main():
    os.makedirs(ROOT / "artifacts", exist_ok=True)
    candidates = []
    with open(SCORED, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f)):
            if i >= LIMIT:
                break
            candidates.append(row)

    existing_urls = load_existing_urls()
    cache = load_cache()
    session = create_shared_session()
    ready = []
    pending = []
    done = 0

    print(f"Discovering URLs for {len(candidates)} candidates (limit {LIMIT})...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(discover_one, c["Nome da Empresa"], c["Segmento da Empresa"], session, cache): c
            for c in candidates
        }
        for future in as_completed(futures):
            done += 1
            res = future.result()
            if res.get("pending"):
                pending.append(res)
            elif res.get("URL") and clean_url(res["URL"]) not in existing_urls:
                ready.append(res)
                existing_urls.add(clean_url(res["URL"]))
            if done % 25 == 0 or done == len(candidates):
                print(f"  {done}/{len(candidates)} | ready={len(ready)} pending={len(pending)}")

    save_cache(cache)

    if ready:
        fields = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL", "evidencia"]
        with open(READY, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(ready)

    if pending:
        with open(PENDING, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["Nome da Empresa", "Segmento da Empresa", "motivo"])
            w.writeheader()
            for p in pending:
                w.writerow(
                    {
                        "Nome da Empresa": p["Nome da Empresa"],
                        "Segmento da Empresa": p["Segmento da Empresa"],
                        "motivo": p.get("motivo", ""),
                    }
                )

    print(f"Ready: {len(ready)} -> {READY}")
    print(f"Pending: {len(pending)} -> {PENDING}")


if __name__ == "__main__":
    main()
