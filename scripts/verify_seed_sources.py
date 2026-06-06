#!/usr/bin/env python3
"""Verifica todas as fontes de seed YAML e gera JSON consolidado."""

from __future__ import annotations

import csv
import json
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

OUT = ROOT / "artifacts/seed_sources_verified.json"
BAD_FRAGMENTS = ("banco.gupy.io", "carreiras.gupy.io/", "portal.gupy.io", "vagas.gupy.io")

SOURCE_FILES = [
    ROOT / "data/seeds/varejo_industria_slugs.yaml",
    ROOT / "data/seeds/b3_slug_aliases.yaml",
]

# Pesquisa web: slugs criativos confirmados (B3 / Valor 1000 / Fortune BR)
WEB_RESEARCHED: list[tuple[str, str, list[str]]] = [
    ("Messer Gases Brasil", "Indústria", ["https://messergases.gupy.io"]),
    ("Evoltz", "Energia e Utilities", ["https://evoltz.gupy.io"]),
    ("Comgás", "Energia e Utilities", ["https://vemsercomgas.gupy.io"]),
    ("Nexa", "Indústria", ["https://vempranexa.gupy.io"]),
    ("VLI Logística", "Logística e Mobilidade", ["https://vli-vagas-externas.gupy.io"]),
    ("Alupar", "Energia e Utilities", ["https://alupar.gupy.io"]),
    ("PRIO", "Energia e Utilities", ["https://prio.gupy.io"]),
    ("Forno de Minas", "Agro e Alimentos", ["https://fornodeminas.gupy.io"]),
    ("Grupo SBF", "Varejo e Consumo", ["https://gruposbftalentos.gupy.io"]),
    ("Hapvida", "Saúde", ["https://hapvidandi.gupy.io"]),
    ("Sem Parar", "Serviços e Outros", ["https://semparar.gupy.io"]),
    ("Multilog", "Logística e Mobilidade", ["https://carreiras.gupy.io/multilog"]),
    ("KMM", "Logística e Mobilidade", ["https://carreiras.gupy.io/kmm"]),
    ("Warren", "Financeiro", ["https://carreiras.gupy.io/warren"]),
    ("Sequoia Logística", "Logística e Mobilidade", ["https://sequoialog.gupy.io"]),
    ("Banco Safra", "Financeiro", ["https://venhasersafra.gupy.io"]),
    ("AgroGalaxy", "Agro e Alimentos", ["https://carreiras.gupy.io/agrogalaxy"]),
    ("GOL Linhas Aéreas", "Logística e Mobilidade", ["https://golcarreiras.gupy.io"]),
    ("Farm Rio", "Varejo e Consumo", ["https://farmrio.gupy.io"]),
    ("Sankhya", "Tecnologia", ["https://sankhya.gupy.io"]),
    ("Indigo", "Logística e Mobilidade", ["https://indigo.gupy.io"]),
    ("Leroy Merlin", "Varejo e Consumo", ["https://leroymerlin.gupy.io"]),
    ("Duratex", "Indústria", ["https://duratex.gupy.io"]),
    ("Tigre", "Indústria", ["https://tigre.gupy.io"]),
    ("Elgin", "Indústria", ["https://elgin.gupy.io"]),
    ("Nidec", "Indústria", ["https://nidec.gupy.io"]),
    ("Whirlpool", "Indústria", ["https://whirlpool.gupy.io"]),
    ("Louis Dreyfus", "Agro e Alimentos", ["https://ldc.gupy.io"]),
    ("Coamo", "Agro e Alimentos", ["https://coamo.gupy.io"]),
    ("Lar Cooperativa", "Agro e Alimentos", ["https://lar.gupy.io"]),
    ("Cotrijal", "Agro e Alimentos", ["https://cotrijal.gupy.io"]),
    ("Cora", "Financeiro", ["https://cora.gupy.io"]),
    ("Genial Investimentos", "Financeiro", ["https://genial.gupy.io"]),
    ("Rossi", "Construção e Imóveis", ["https://rossi.gupy.io"]),
    ("Direcional", "Construção e Imóveis", ["https://direcionalengenharia.gupy.io"]),
    ("Cury", "Construção e Imóveis", ["https://cury.gupy.io"]),
    ("Unimed BH", "Saúde", ["https://unimedbh.gupy.io"]),
    ("Unimed Rio", "Saúde", ["https://unimedrio.gupy.io"]),
    ("Grupo NotreDame Intermédica", "Saúde", ["https://gndi.gupy.io"]),
    ("Bluemed", "Saúde", ["https://bluemed.gupy.io"]),
    ("Nissei", "Saúde", ["https://nissei.gupy.io"]),
    ("Shopee Brasil", "Varejo e Consumo", ["https://shopee.gupy.io"]),
    ("Cabify", "Logística e Mobilidade", ["https://cabify.gupy.io"]),
    ("Warner Bros Discovery", "Mídia e Entretenimento", ["https://warnerbrosdiscovery.gupy.io"]),
    ("Uniderp", "Educação", ["https://uniderp.gupy.io"]),
    ("Uniasselvi", "Educação", ["https://uniasselvi.gupy.io"]),
    ("Descomplica", "Educação", ["https://descomplica.gupy.io"]),
    ("Arco Educação", "Educação", ["https://arcoeducacao.gupy.io"]),
    ("Vitru", "Educação", ["https://vitru.gupy.io"]),
    ("FAAP", "Educação", ["https://faap.gupy.io"]),
    ("Mackenzie", "Educação", ["https://mackenzie.gupy.io"]),
    ("Enel Distribuição", "Energia e Utilities", ["https://eneldistribuicao.gupy.io"]),
    ("Corsan", "Energia e Utilities", ["https://corsan.gupy.io"]),
    ("Youcom", "Varejo e Consumo", ["https://youcom.gupy.io"]),
    ("Tintas Coral", "Varejo e Consumo", ["https://coral.gupy.io"]),
    ("Allos", "Varejo e Consumo", ["https://allos.gupy.io"]),
    ("Paramount Brasil", "Mídia e Entretenimento", ["https://paramount.gupy.io"]),
    ("Guide Investimentos", "Financeiro", ["https://guide.gupy.io"]),
    ("Mirae Asset", "Financeiro", ["https://miraeasset.gupy.io"]),
    ("SulAmérica Saúde", "Saúde", ["https://sulamericaseguros.gupy.io"]),
    ("Metalfrio", "Indústria", ["https://metalfrio.gupy.io"]),
    ("Mahle", "Indústria", ["https://mahle.gupy.io"]),
    ("PwC Brasil", "Serviços e Outros", ["https://www.pwc.com.br/pt/carreira-na-pwc.html"]),
    ("BCG Brasil", "Serviços e Outros", ["https://careers.bcg.com/global/en/locations/brazil"]),
    ("Bain Brasil", "Serviços e Outros", ["https://www.bain.com/careers"]),
    ("McKinsey Brasil", "Serviços e Outros", ["https://www.mckinsey.com/br/careers-in-brazil"]),
    ("Western Union Brasil", "Financeiro", ["https://careers.westernunion.com"]),
    ("ManpowerGroup Brasil", "Serviços e Outros", ["https://www.manpowergroup.com/careers"]),
    ("Atos Brasil", "Tecnologia", ["https://atos.net/en/careers"]),
    ("DXC Brasil", "Tecnologia", ["https://careers.dxc.com"]),
    ("MongoDB Brasil", "Tecnologia", ["https://www.mongodb.com/careers"]),
    ("Snowflake Brasil", "Tecnologia", ["https://careers.snowflake.com"]),
    ("Stripe Brasil", "Tecnologia", ["https://stripe.com/jobs"]),
    ("Twilio Brasil", "Tecnologia", ["https://jobs.twilio.com"]),
    ("Wipro Brasil", "Tecnologia", ["https://careers.wipro.com"]),
    ("Palo Alto Networks Brasil", "Tecnologia", ["https://jobs.paloaltonetworks.com"]),
    ("Unisys Brasil", "Tecnologia", ["https://www.unisys.com/careers"]),
    ("TCS Brasil", "Tecnologia", ["https://www.tcs.com/careers"]),
    ("EF Brasil", "Educação", ["https://careers.ef.com"]),
    ("Disney Brasil", "Mídia e Entretenimento", ["https://jobs.disneycareers.com"]),
    ("Gympass", "Serviços e Outros", ["https://boards.greenhouse.io/gympass"]),
    ("Sinqia", "Tecnologia", ["https://jobs.quickin.io/sinqia/jobs"]),
    ("Expresso São Miguel", "Logística e Mobilidade", ["https://sejaesm.gupy.io"]),
    ("Blue3", "Financeiro", ["https://vemserblue3.gupy.io"]),
    ("Fortbras", "Varejo e Consumo", ["https://fortbras.gupy.io"]),
    ("Grupo JCPM", "Mídia e Entretenimento", ["https://grupojcpm.gupy.io"]),
    ("MR3", "Logística e Mobilidade", ["https://mr3-operadorlogistico.gupy.io"]),
    ("Saint-Gobain Brasil", "Indústria", ["https://saintgobainbrasil.gupy.io"]),
    ("Veolia Brasil", "Energia e Utilities", ["https://carreirasveo.gupy.io"]),
    ("Mahindra Brasil", "Indústria", ["https://mahindra.gupy.io"]),
    ("CS Infra", "Construção e Imóveis", ["https://csinfra.gupy.io"]),
    ("ioasys", "Tecnologia", ["https://ioasys.gupy.io"]),
    ("CoE Votorantim", "Indústria", ["https://votorantimcoe.gupy.io"]),
    ("Hyva do Brasil", "Indústria", ["https://hyvadobrasil.gupy.io"]),
    ("Nio", "Energia e Utilities", ["https://nio.gupy.io"]),
    ("Expresso Nepomuceno", "Logística e Mobilidade", ["https://en.gupy.io"]),
    ("Bemol", "Varejo e Consumo", ["https://bemol.gupy.io"]),
    ("Repassa", "Varejo e Consumo", ["https://repassa.gupy.io"]),
    ("Portobello Shop", "Varejo e Consumo", ["https://portobelloshop.gupy.io"]),
    ("Even", "Construção e Imóveis", ["https://sejaeven.gupy.io"]),
    ("Track&Field", "Varejo e Consumo", ["https://tfcarreira.gupy.io"]),
    ("RSM Brasil", "Serviços e Outros", ["https://rsmbrasil.gupy.io"]),
    ("Encantech", "Tecnologia", ["https://encantech.gupy.io"]),
    ("Maria Filó", "Varejo e Consumo", ["https://mariafilo.gupy.io"]),
    ("Estadão", "Mídia e Entretenimento", ["https://estadao.gupy.io"]),
    ("Porto Sudeste", "Logística e Mobilidade", ["https://porto.gupy.io"]),
]


def load_excluded() -> tuple[set[str], set[str]]:
    names: set[str] = set()
    with open(ROOT / "data/seeds/known_career_urls.yaml", encoding="utf-8") as f:
        for c in yaml.safe_load(f).get("companies", []):
            names.add(normalize_name(c["name"]))
    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(normalize_name(row["Nome da Empresa"]))
    patch = ROOT / "artifacts/known_career_urls_patch.yaml"
    if patch.exists():
        for m in re.finditer(r"- name: (.+)", patch.read_text(encoding="utf-8")):
            names.add(normalize_name(m.group(1)))

    urls: set[str] = set()
    with open(ROOT / "src/data/input/list.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            urls.add(clean_url(row["URL"]))
    return names, urls


def load_yaml_sources() -> list[tuple[str, str, list[str]]]:
    items: list[tuple[str, str, list[str]]] = []
    for path in SOURCE_FILES:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for key in ("companies", "aliases"):
            for c in data.get(key, []):
                name = c["name"]
                macro = c.get("macro", "Serviços e Outros")
                urls = c.get("urls", [])
                if urls:
                    items.append((name, macro, urls))
    items.extend(WEB_RESEARCHED)
    return items


def is_bad(url: str) -> bool:
    return any(b in url.lower() for b in BAD_FRAGMENTS)


def verify_one(name: str, macro: str, urls: list[str], session) -> dict | None:
    for url in urls:
        if is_bad(url):
            continue
        url = clean_url(url)
        if verify_website_status(session, url)["status"] != "1":
            continue
        if not verify_portal_has_jobs(url, session):
            continue
        good = [url]
        for u in urls:
            u = clean_url(u)
            if u != url and not is_bad(u):
                good.append(u)
            if len(good) >= 3:
                break
        return {"name": name, "macro": macro, "urls": good[:3]}
    return None


def main() -> None:
    excluded_names, excluded_urls = load_excluded()
    candidates: list[tuple[str, str, list[str]]] = []
    seen: set[str] = set()

    for name, macro, urls in load_yaml_sources():
        key = normalize_name(name)
        if not key or key in seen or key in excluded_names:
            continue
        primary = clean_url(urls[0])
        if primary in excluded_urls:
            continue
        seen.add(key)
        candidates.append((name, macro, urls))

    print(f"Verificando {len(candidates)} candidatos...")
    session = create_shared_session()
    verified: list[dict] = []

    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(verify_one, n, m, u, session): n for n, m, u in candidates}
        for fut in as_completed(futs):
            res = fut.result()
            if res:
                verified.append(res)
                print(f"+ [{len(verified)}] {res['name']} -> {res['urls'][0]}")

    OUT.write_text(json.dumps(verified, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"DONE: {len(verified)} -> {OUT}")


if __name__ == "__main__":
    main()
