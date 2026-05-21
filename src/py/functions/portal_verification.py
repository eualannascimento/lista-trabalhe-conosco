"""Verificação forte de portais de carreira (além de HTTP 200)."""

import json
import re
from urllib.parse import urlparse

import requests

from .website_verification import create_shared_session

JOB_KEYWORDS = re.compile(
    r"vagas?|oportunidades|carreiras|trabalhe|jobs|emprego|candidate|inscri",
    re.I,
)

GENERIC_GUPY_TITLES = (
    "página de carreiras eurochem",
    "404",
    "gupy",
    "portal de vagas",
)


def _fetch_page(session, url: str, timeout: int = 12) -> tuple[str | None, str]:
    """Retorna (html, url_final após redirects)."""
    try:
        resp = session.get(url, timeout=timeout, allow_redirects=True, verify=True)
        if 200 <= resp.status_code < 400:
            return resp.text[:500_000], resp.url or url
    except requests.RequestException:
        pass
    return None, url


def _parse_next_data(html: str) -> dict:
    m = re.search(
        r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',
        html,
        re.S,
    )
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return {}


def _gupy_job_count(page_props: dict) -> int:
    if not page_props:
        return 0
    for key in ("jobs", "jobList", "openJobs", "vacancies"):
        val = page_props.get(key)
        if isinstance(val, list) and val:
            return len(val)
    job = page_props.get("job")
    if isinstance(job, dict) and job.get("id"):
        return 1
    return 0


def _gupy_is_generic_portal(final_url: str, html: str, requested_url: str) -> bool:
    """Detecta redirect para portal genérico carreiras.gupy.io (sem empresa)."""
    parsed = urlparse(final_url.lower().rstrip("/"))
    req_path = urlparse(requested_url.lower()).path.strip("/")

    # carreiras.gupy.io/{slug} que vira só / ou /pt sem o slug
    if "carreiras.gupy.io" in parsed.netloc:
        path = parsed.path.strip("/")
        if not path or path in ("pt", "en", "jobs"):
            if req_path and req_path not in path:
                return True

    title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
    if title_m:
        title = title_m.group(1).strip().lower()
        if any(g in title for g in GENERIC_GUPY_TITLES):
            return True

    return False


def _gupy_has_jobs(html: str, final_url: str, requested_url: str) -> bool:
    if not html:
        return False
    if _gupy_is_generic_portal(final_url, html, requested_url):
        return False

    data = _parse_next_data(html)
    page_props = data.get("props", {}).get("pageProps", {}) if data else {}
    if _gupy_job_count(page_props) > 0:
        return True

    # Subdomínio dedicado com título da empresa (não 404 genérico)
    host = urlparse(final_url).netloc.lower()
    if host.endswith(".gupy.io") and host not in (
        "carreiras.gupy.io",
        "portal.gupy.io",
        "www.gupy.io",
    ):
        title_m = re.search(r"<title>([^<]+)</title>", html, re.I)
        if title_m and title_m.group(1).strip().lower() not in GENERIC_GUPY_TITLES:
            if JOB_KEYWORDS.search(html):
                return True

    return False


def _greenhouse_has_jobs(html: str | None, final_url: str, session) -> bool:
    """Greenhouse: aceita portal com vagas ou HEAD 200 em job-boards."""
    if html and _generic_has_jobs(html):
        return True
    try:
        head = session.head(final_url, timeout=10, allow_redirects=True, verify=True)
        if 200 <= head.status_code < 400:
            return True
        if head.status_code == 406 and "greenhouse.io" in final_url.lower():
            return True
    except requests.RequestException:
        pass
    return False


def _generic_has_jobs(html: str) -> bool:
    if not html:
        return False
    hits = len(JOB_KEYWORDS.findall(html))
    return hits >= 2 or (
        hits >= 1
        and re.search(r"apply|candidat|inscri|search|requisition|opening", html, re.I)
    )


def verify_portal_has_jobs(url: str, session=None) -> bool:
    """
    Retorna True se o portal parece um site de vagas real.
    """
    if not url or not url.startswith("http"):
        return False

    own_session = session is None
    if own_session:
        session = create_shared_session()

    html, final_url = _fetch_page(session, url)
    if not html:
        if own_session:
            session.close()
        return False

    u = url.lower()
    ok = False
    if "gupy.io" in u:
        ok = _gupy_has_jobs(html, final_url, url)
    elif "greenhouse.io" in u:
        ok = _greenhouse_has_jobs(html, final_url, session)
    elif any(
        x in u
        for x in (
            "myworkdayjobs.com",
            "lever.co",
            "inhire",
            "successfactors",
            "pandape.infojobs",
            "vagas.com.br",
            "workable.com",
        )
    ):
        ok = _generic_has_jobs(html)
    else:
        ok = _generic_has_jobs(html)

    if own_session:
        session.close()
    return ok
