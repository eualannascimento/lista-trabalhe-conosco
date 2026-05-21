#!/usr/bin/env python3
"""
Corrige URLs inativas (status 0), remove duplicatas óbvias e insere empresas novas
no mesmo perfil da lista (Gupy/InHire/Greenhouse, grandes empregadores BR).
"""

import csv
import importlib.util
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.segment_macro_map import to_macro
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import (
    create_shared_session,
    verify_website_status,
)

_guesser_path = os.path.join(os.path.dirname(__file__), "fix_vagas_urls_guesser.py")
_spec = importlib.util.spec_from_file_location("fix_vagas_urls_guesser", _guesser_path)
_guesser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_guesser)

LIST_PATH = os.path.join(ROOT, "src/data/input/list.csv")
REPORT_PATH = os.path.join(ROOT, "artifacts/fix_inactive_report.csv")
FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
]

# Inativas redundantes quando já existe portal ativo equivalente na lista
REMOVE_IF_ACTIVE_URL_EXISTS = {
    "Azul Linhas Aéreas": "https://voeazul.gupy.io",
    "Banco Safra": "https://venhasersafra.gupy.io",
    "Itaú Unibanco": "https://vemproitau.gupy.io",
    "C&A Brasil": "https://cea.gupy.io",
}

# Correções manuais (nome exato -> URL canônica verificada em rodadas anteriores / pares ativos)
KNOWN_URL_FIXES = {
    "Magazine Luiza": "https://magazineluiza.inhire.app",
    "B3": "https://carreiras.gupy.io/b3",
    "TIM Brasil": "https://carreiras.gupy.io/tim",
    "Havan": "https://carreiras.gupy.io/havan",
    "BRF": "https://carreiras.gupy.io/brf",
    "Smart Fit": "https://carreiras.gupy.io/smartfit",
    "Tramontina": "https://carreiras.gupy.io/tramontina",
    "MRV": "https://carreiras.gupy.io/mrv",
    "Ultrapar": "https://carreiras.gupy.io/ultrapar",
    "CPFL Energia": "https://carreiras.gupy.io/cpfl",
    "Eneva": "https://carreiras.gupy.io/eneva",
    "Copel": "https://carreiras.gupy.io/copel",
    "Carrefour Brasil": "https://carreiras.gupy.io/carrefour",
    "Grupo Mateus": "https://carreiras.gupy.io/grupomateus",
    "Grendene": "https://carreiras.gupy.io/grendene",
    "Marfrig": "https://carreiras.gupy.io/marfrig",
    "Raízs": "https://carreiras.gupy.io/raizs",
    "PicPay": "https://carreiras.gupy.io/picpay",
    "XP Banco": "https://carreiras.gupy.io/xpinc",
    "Itaú Unibanco": "https://vempra.gupy.io/itau",
    "Azul Linhas Aéreas": "https://voeazul.gupy.io",
    "C&A Brasil": "https://cea.gupy.io",
    "Banco Safra": "https://venhasersafra.gupy.io",
    "PagBank (PagSeguro)": "https://carreiras.gupy.io/pagbank",
    "Loggi Tecnologia": "https://carreiras.gupy.io/loggi",
    "Grupo Fleury": "https://carreiras.gupy.io/fleury",
    "Fleury": "https://grupofleury.gupy.io",
    "Ticket (Edenred Brasil)": "https://carreiras.gupy.io/edenred",
    "Sodexo (Pluxee Brasil)": "https://pluxee.gupy.io",
    "Sem Parar": "https://semparar.gupy.io",
    "Getnet": "https://carreiras.gupy.io/getnet",
    "Livelo": "https://carreiras.gupy.io/livelo",
    "Enjoei": "https://carreiras.gupy.io/enjoei",
    "AgroGalaxy": "https://carreiras.gupy.io/agrogalaxy",
    "Multilog": "https://carreiras.gupy.io/multilog",
    "KMM": "https://carreiras.gupy.io/kmm",
    "Warren": "https://carreiras.gupy.io/warren",
    "Neon": "https://jobs.lever.co/neon",
    "Banco Original": "https://original.gupy.io",
    "99 (99Entrega)": "https://carreiras.gupy.io/99",
    "DiDi (99)": "https://carreiras.gupy.io/99",
}

# Novas empresas no perfil da lista (mesmos setores/plataformas que entradas ativas)
NEW_BY_PROFILE = [
    ("Oi", "Energia e Utilities", ["https://carreiras.gupy.io/oi", "https://oi.gupy.io"]),
    ("Zenvia", "Tecnologia", ["https://zenvia.gupy.io", "https://carreiras.gupy.io/zenvia"]),
    ("LWSA", "Tecnologia", ["https://lwsa.gupy.io", "https://carreiras.gupy.io/lwsa"]),
    ("Sicoob", "Financeiro", ["https://sicredi.gupy.io", "https://carreiras.gupy.io/sicoob"]),
    ("Unicred Centro-Oeste", "Financeiro", ["https://unicred.gupy.io"]),
    ("Algar Telecom", "Energia e Utilities", ["https://algar.gupy.io", "https://carreiras.gupy.io/algar"]),
    ("Grupo Salta", "Educação", ["https://carreiras.gupy.io/salta", "https://salta.gupy.io"]),
    ("Yduqs", "Educação", ["https://yduqs.gupy.io"]),
    ("Anima Holding", "Educação", ["https://anima.gupy.io"]),
    ("Cogna Educação", "Educação", ["https://cogna.gupy.io"]),
    ("Localiza", "Logística e Mobilidade", ["https://localiza.gupy.io"]),
    ("Movida", "Logística e Mobilidade", ["https://movida.gupy.io"]),
    ("Unidas", "Logística e Mobilidade", ["https://unidas.gupy.io"]),
    ("Porto Seguro", "Financeiro", ["https://porto.gupy.io"]),
    ("SulAmérica", "Financeiro", ["https://sulamerica.gupy.io", "https://carreiras.gupy.io/sulamerica"]),
    ("Mapfre", "Financeiro", ["https://carreiras.gupy.io/mapfre"]),
    ("Allianz", "Financeiro", ["https://carreiras.gupy.io/allianz"]),
    ("Sompo Seguros", "Financeiro", ["https://sompo.gupy.io"]),
    ("Agibank", "Financeiro", ["https://job-boards.greenhouse.io/agibank"]),
    ("Banco BS2", "Financeiro", ["https://bs2.gupy.io", "https://bancobs2.gupy.io"]),
    ("Banco Modal", "Financeiro", ["https://modal.gupy.io"]),
    ("Crefisa", "Financeiro", ["https://crefisa.gupy.io"]),
    ("Omni", "Financeiro", ["https://omni.gupy.io"]),
    ("Will Bank", "Financeiro", ["https://willbank.inhire.app/vagas"]),
    ("C&A", "Varejo e Consumo", ["https://cea.gupy.io"]),
    ("Arezzo", "Varejo e Consumo", ["https://azzas2154.gupy.io"]),
    ("Grupo Soma", "Varejo e Consumo", ["https://gruposoma.gupy.io"]),
    ("Track&Field", "Varejo e Consumo", ["https://tfcarreira.gupy.io"]),
    ("Hering", "Varejo e Consumo", ["https://ciahering.gupy.io", "https://hering.gupy.io"]),
    ("Alpargatas", "Varejo e Consumo", ["https://alpargatas.gupy.io"]),
    ("Natura", "Varejo e Consumo", ["https://natura.gupy.io", "https://avon.gupy.io"]),
    ("Boticário", "Varejo e Consumo", ["https://grupoboticario.gupy.io"]),
    ("Pernambucanas", "Varejo e Consumo", ["https://pernambucanas.gupy.io"]),
    ("Marisa", "Varejo e Consumo", ["https://carreiras.gupy.io/marisa"]),
    ("Tok&Stok", "Varejo e Consumo", ["https://tokstok.pandape.infojobs.com.br"]),
    ("Decathlon", "Varejo e Consumo", ["https://carreirasdecathlon.gupy.io"]),
    ("Petz", "Varejo e Consumo", ["https://petz.gupy.io"]),
    ("Cobasi", "Varejo e Consumo", ["https://cobasi.pandape.infojobs.com.br"]),
    ("Raia Drogasil", "Saúde", ["https://carreiras.gupy.io/rd"]),
    ("Fleury", "Saúde", ["https://grupofleury.gupy.io", "https://carreiras.gupy.io/fleury"]),
    ("Dasa", "Saúde", ["https://carreiras.gupy.io/dasa"]),
    ("Rede D'Or", "Saúde", ["https://rededor.gupy.io"]),
    ("Einstein", "Saúde", ["https://einstein.gupy.io", "https://carreiras.gupy.io/einstein"]),
    ("Prevent Senior", "Saúde", ["https://www.preventsenior.com.br/trabalhe-conosco"]),
    ("EMS", "Saúde", ["https://ems.izirh.io"]),
    ("Aché", "Saúde", ["https://vagasache.gupy.io"]),
    ("Eurofarma", "Saúde", ["https://eurofarma.gupy.io"]),
    ("Klabin", "Indústria", ["https://klabin.inhire.app/vagas"]),
    ("Suzano", "Indústria", ["https://suzano.gupy.io"]),
    ("Fibria", "Indústria", ["https://suzano.gupy.io"]),
    ("Gerdau", "Indústria", ["https://career19.sapsf.com/careers?company=gerdauacos"]),
    ("Usiminas", "Indústria", ["https://usiminas.gupy.io"]),
    ("ArcelorMittal", "Indústria", ["https://tuper.gupy.io"]),
    ("WEG", "Indústria", ["https://weg.gupy.io"]),
    ("Embraer", "Indústria", ["https://embraer.gupy.io"]),
    ("Randon", "Indústria", ["https://randon.gupy.io"]),
    ("Tupy", "Indústria", ["https://tupy.gupy.io"]),
    ("Stellantis", "Indústria", ["https://careers.stellantis.com"]),
    ("Volkswagen", "Indústria", ["https://carreiras.gupy.io/volkswagen"]),
    ("Toyota", "Indústria", ["https://carreiras.gupy.io/toyota"]),
    ("Honda", "Indústria", ["https://honda.gupy.io"]),
    ("Yamaha", "Indústria", ["https://yamaha.gupy.io"]),
    ("Raízen", "Energia e Utilities", ["https://genteraizen.gupy.io"]),
    ("Ipiranga", "Energia e Utilities", ["https://ipiranga.gupy.io"]),
    ("Vibra", "Energia e Utilities", ["https://vibraenergia.gupy.io"]),
    ("Equatorial", "Energia e Utilities", ["https://equatorialenergia.gupy.io"]),
    ("AES Brasil", "Energia e Utilities", ["https://carreiras.gupy.io/aes"]),
    ("Engie", "Energia e Utilities", ["https://jobs.engie.com"]),
    ("EDP", "Energia e Utilities", ["https://jobs.edp.com"]),
    ("Copel", "Energia e Utilities", ["https://carreiras.gupy.io/copel"]),
    ("Celesc", "Energia e Utilities", ["https://www.celesc.com.br/trabalhe-na-celesc"]),
    ("BRK Ambiental", "Energia e Utilities", ["https://brk.gupy.io"]),
    ("Aegea", "Energia e Utilities", ["https://aegea.gupy.io"]),
    ("JBS", "Agro e Alimentos", ["https://grupojbs.gupy.io"]),
    ("Marfrig", "Agro e Alimentos", ["https://marfrig.gupy.io", "https://carreiras.gupy.io/marfrig"]),
    ("Minerva", "Agro e Alimentos", ["https://minervafoods.gupy.io"]),
    ("Bauducco", "Agro e Alimentos", ["https://bauducco.gupy.io"]),
    ("Piracanjuba", "Agro e Alimentos", ["https://piracanjuba.gupy.io"]),
    ("Camil", "Agro e Alimentos", ["https://platform.senior.com.br/hcmrs/hcm/curriculo/?tenant=camilcombr"]),
    ("Ambev", "Agro e Alimentos", ["https://ambev.gupy.io"]),
    ("Heineken", "Agro e Alimentos", ["https://careers.theheinekencompany.com/Brazil/search"]),
    ("BRF", "Agro e Alimentos", ["https://carreiras.gupy.io/brf"]),
    ("BRQ", "Tecnologia", ["https://carreiras.gupy.io/brq"]),
    ("Stefanini", "Tecnologia", ["https://stefanini.gupy.io"]),
    ("Totvs", "Tecnologia", ["https://carreiras.gupy.io/totvs"]),
    ("Linx", "Tecnologia", ["https://carreiras.gupy.io/linx"]),
    ("Locaweb", "Tecnologia", ["https://locaweb.gupy.io"]),
    ("VTEX", "Tecnologia", ["https://job-boards.greenhouse.io/vtex"]),
    ("RD Station", "Tecnologia", ["https://boards.greenhouse.io/rdstation"]),
    ("Stone", "Tecnologia", ["https://stone.gupy.io"]),
    ("PagSeguro", "Financeiro", ["https://pagseguro.gupy.io"]),
    ("Nubank", "Financeiro", ["https://boards.greenhouse.io/nubank"]),
    ("Inter", "Financeiro", ["https://boards.greenhouse.io/inter"]),
    ("C6 Bank", "Financeiro", ["https://boards.greenhouse.io/c6bank"]),
    ("BTG Pactual", "Financeiro", ["https://boards.greenhouse.io/btgpactual"]),
    ("XP Inc", "Financeiro", ["https://boards.greenhouse.io/xpinc"]),
    ("QuintoAndar", "Construção e Imóveis", ["https://boards.greenhouse.io/quintoandar"]),
    ("Cyrela", "Construção e Imóveis", ["https://cyrela.gupy.io"]),
    ("Tenda", "Construção e Imóveis", ["https://tenda.gupy.io"]),
    ("Mitre", "Construção e Imóveis", ["https://mitrerealty.gupy.io"]),
    ("Rumo", "Logística e Mobilidade", ["https://rumolog.gupy.io"]),
    ("JSL", "Logística e Mobilidade", ["https://jsl.gupy.io"]),
    ("Total Express", "Logística e Mobilidade", ["https://totalexpress.gupy.io"]),
    ("Correios", "Logística e Mobilidade", ["https://correios.gupy.io"]),
    ("Sequoia Logística", "Logística e Mobilidade", ["https://sequoialog.gupy.io"]),
    ("Globo", "Mídia e Entretenimento", ["https://globo.gupy.io"]),
    ("Record", "Mídia e Entretenimento", ["https://recordtv.gupy.io"]),
    ("Band", "Mídia e Entretenimento", ["https://band.jobs.recrut.ai/#openings"]),
    ("UOL", "Mídia e Entretenimento", ["https://uol.gupy.io"]),
    ("Wildlife", "Mídia e Entretenimento", ["https://boards.greenhouse.io/wildlifestudios"]),
]


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "", name.lower())
    return s[:40]


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
    if "izirh" in u:
        return "IziRH"
    return "Site da Empresa"


def verify_url(session, url: str, strong: bool = True) -> bool:
    url = clean_url(url)
    if verify_website_status(session, url)["status"] != "1":
        return False
    if strong:
        return verify_portal_has_jobs(url, session)
    return True


def resolve_url(session, name: str, candidates: list[str]) -> str | None:
    for url in candidates:
        if verify_url(session, url):
            return clean_url(url)
    found = _guesser.is_valid_ats(name)
    if found and verify_url(session, found):
        return clean_url(found)
    slug = slugify(name)
    extra = [
        f"https://{slug}.gupy.io",
        f"https://carreiras.gupy.io/{slug}",
    ]
    for url in extra:
        if verify_url(session, url):
            return clean_url(url)
    return None


def load_rows():
    with open(LIST_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_rows(rows):
    with open(LIST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    os.makedirs(os.path.join(ROOT, "artifacts"), exist_ok=True)
    rows = load_rows()
    session = create_shared_session()
    today = date.today().strftime("%Y-%m-%d")
    report = []

    active_urls = {clean_url(r["URL"]) for r in rows if r["Status da URL"] == "1"}
    existing_names = {r["Nome da Empresa"].strip().lower() for r in rows}
    existing_urls = {clean_url(r["URL"]) for r in rows}

    # --- Remover duplicatas óbvias ---
    kept = []
    removed = 0
    for row in rows:
        name = row["Nome da Empresa"]
        if name in REMOVE_IF_ACTIVE_URL_EXISTS:
            canon = clean_url(REMOVE_IF_ACTIVE_URL_EXISTS[name])
            if canon in active_urls:
                report.append({"Empresa": name, "Acao": "removed_duplicate", "URL": row["URL"], "Detalhe": canon})
                removed += 1
                continue
        kept.append(row)
    rows = kept
    print(f"Removidas {removed} duplicatas")

    # --- Corrigir inativas ---
    fixed = 0
    for row in rows:
        if row["Status da URL"] != "0":
            continue
        name = row["Nome da Empresa"]
        old_url = clean_url(row["URL"])
        new_url = None
        action = "still_inactive"

        if name in KNOWN_URL_FIXES:
            candidate = clean_url(KNOWN_URL_FIXES[name])
            if verify_url(session, candidate):
                new_url = candidate

        if not new_url:
            slug = slugify(name)
            guesses = [
                f"https://carreiras.gupy.io/{slug}",
                f"https://{slug}.gupy.io",
            ]
            new_url = resolve_url(session, name, guesses)

        if new_url and new_url != old_url:
            row["URL"] = new_url
            row["Plataforma"] = detect_platform(new_url)
            row["Status da URL"] = "1"
            fixed += 1
            action = "fixed"
        elif new_url:
            row["URL"] = new_url
            row["Plataforma"] = detect_platform(new_url)
            if verify_url(session, new_url):
                row["Status da URL"] = "1"
                fixed += 1
                action = "verified_same"

        report.append({"Empresa": name, "Acao": action, "URL": row["URL"], "Detalhe": old_url})

    print(f"Corrigidas/reativadas {fixed} inativas")

    # --- Novas empresas (perfil da lista) ---
    added = 0
    for name, macro, candidates in NEW_BY_PROFILE:
        key = name.strip().lower()
        if key in existing_names:
            continue
        url = resolve_url(session, name, candidates)
        if not url or url in existing_urls:
            continue
        rows.append(
            {
                "Status da URL": "1",
                "Data de Entrada": today,
                "Nome da Empresa": name,
                "Segmento da Empresa": macro,
                "Plataforma": detect_platform(url),
                "URL": url,
            }
        )
        existing_names.add(key)
        existing_urls.add(url)
        added += 1
        report.append({"Empresa": name, "Acao": "added_new", "URL": url, "Detalhe": macro})
        print(f"+ {name} -> {url}")

    print(f"Adicionadas {added} empresas novas")

    with open(REPORT_PATH, "w", newline="", encoding="utf-8") as f:
        if report:
            writer = csv.DictWriter(f, fieldnames=report[0].keys())
            writer.writeheader()
            writer.writerows(report)

    save_rows(rows)
    active = sum(1 for r in rows if r["Status da URL"] == "1")
    inactive = sum(1 for r in rows if r["Status da URL"] == "0")
    print(f"Total {len(rows)} | ativas {active} | inativas {inactive}")
    print(f"Relatório: {REPORT_PATH}")


if __name__ == "__main__":
    main()
