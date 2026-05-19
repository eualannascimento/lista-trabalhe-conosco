"""Shared URL repair helpers for lista-trabalhe-conosco."""

import re
from urllib.parse import urlparse

import requests
import urllib3
from unidecode import unidecode

urllib3.disable_warnings()

GENERIC_GUPY_ROOTS = {
    "https://carreiras.gupy.io",
    "https://portal.gupy.io",
}

SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
    }
)


def slugify_name(name: str) -> str:
    s = unidecode(name.lower())
    return re.sub(r"[^a-z0-9]+", "", s)


def slug_variants(name: str, current_url: str = "") -> list[str]:
    base = slugify_name(name)
    variants = [base]
    if base.startswith("grupo"):
        variants.append(base[5:])
    else:
        variants.append(f"grupo{base}")
    variants.append(f"{base}brasil")

    match = re.search(r"https://([^.]+)\.gupy\.io", current_url or "")
    if match:
        variants.insert(0, match.group(1))

    seen = set()
    out = []
    for v in variants:
        if v and v not in seen:
            seen.add(v)
            out.append(v)
    return out


def is_reachable_url(url: str, timeout: int = 5) -> bool:
    try:
        response = SESSION.head(
            url, timeout=timeout, allow_redirects=True, verify=False
        )
        if response.status_code == 405:
            response = SESSION.get(
                url, timeout=timeout, allow_redirects=True, verify=False
            )
        if response.status_code >= 400 and response.status_code not in (403, 408):
            return False
        final = response.url.lower().rstrip("/")
        if final in GENERIC_GUPY_ROOTS:
            return False
        return True
    except requests.RequestException:
        return False


def normalize_final_url(url: str, timeout: int = 5) -> str | None:
    if not is_reachable_url(url, timeout=timeout):
        return None
    try:
        response = SESSION.head(
            url, timeout=timeout, allow_redirects=True, verify=False
        )
        if response.status_code == 405:
            response = SESSION.get(
                url, timeout=timeout, allow_redirects=True, verify=False
            )
        return response.url.rstrip("/")
    except requests.RequestException:
        return None


def gupy_candidate_urls(name: str, current_url: str = "") -> list[str]:
    candidates = []
    for slug in slug_variants(name, current_url):
        candidates.extend(
            [
                f"https://{slug}.gupy.io",
                f"https://grupo{slug}.gupy.io" if not slug.startswith("grupo") else f"https://{slug}.gupy.io",
                f"https://carreiras.gupy.io/{slug}",
                f"https://talent.gupy.io/{slug}",
            ]
        )
    # dedupe preserving order
    seen = set()
    out = []
    for url in candidates:
        key = url.lower()
        if key not in seen:
            seen.add(key)
            out.append(url)
    return out


def ats_candidate_urls(name: str) -> list[str]:
    """Kenoby, Solides, Empregare, Gupy subdomains from company name."""
    bases = slug_variants(name)
    candidates = []
    for b in bases:
        if not b:
            continue
        candidates.extend(
            [
                f"https://{b}.gupy.io",
                f"https://grupo{b}.gupy.io",
                f"https://jobs.kenoby.com/{b}",
                f"https://{b}.solides.jobs",
                f"https://{b}.empregare.com/pt-br",
            ]
        )
    return list(dict.fromkeys(candidates))


def infer_platform(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if "gupy.io" in host:
        return "Gupy"
    if "kenoby.com" in host:
        return "Kenoby"
    if "solides" in host:
        return "Solides"
    if "empregare.com" in host:
        return "Empregare"
    if "greenhouse.io" in host:
        return "Greenhouse"
    if "myworkdayjobs.com" in host or "workdaysite.com" in host:
        return "Workday"
    return "Vagas"


def find_replacement_url(name: str, current_url: str) -> str | None:
    current_norm = current_url.lower().rstrip("/")
    for url in gupy_candidate_urls(name, current_url) + ats_candidate_urls(name):
        if url.lower().rstrip("/") == current_norm:
            continue
        final = normalize_final_url(url)
        if final and final.lower().rstrip("/") != current_norm:
            if "gupy.io" in final and final.rstrip("/") in GENERIC_GUPY_ROOTS:
                continue
            return final
    return None
