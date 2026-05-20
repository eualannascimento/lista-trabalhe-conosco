#!/usr/bin/env python3
"""Adiciona empresas verificadas que ainda não estão no list.csv."""

import csv
import importlib.util
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from scripts.segment_macro_map import to_macro
from src.py.functions.df_operations import clean_url
from src.py.functions.website_verification import create_shared_session, verify_website_status

_guesser_path = os.path.join(os.path.dirname(__file__), "fix_vagas_urls_guesser.py")
_spec = importlib.util.spec_from_file_location("fix_vagas_urls_guesser", _guesser_path)
_guesser = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_guesser)

LIST_PATH = os.path.join(ROOT, "src/data/input/list.csv")
FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
]

# nome, segmento detalhado (será macro), plataforma sugerida, URLs candidatas em ordem
CANDIDATES = [
    ("Claro Brasil", "Telecom", "Gupy", ["https://claro.gupy.io", "https://carreiras.gupy.io/claro"]),
    ("Intelbras", "Tecnologia", "Gupy", ["https://intelbras.gupy.io"]),
    ("Atacadão", "Varejo", "Gupy", ["https://atacadao.gupy.io", "https://carreiras.gupy.io/atacadao"]),
    ("Grupo Pão de Açúcar", "Varejo", "Gupy", ["https://gpabr.gupy.io", "https://paodeacucar.gupy.io"]),
    ("BrMalls", "Shopping", "Gupy", ["https://brmalls.gupy.io"]),
    ("Valid", "Tecnologia", "Gupy", ["https://valid.gupy.io"]),
    ("Multilaser", "Tecnologia", "Gupy", ["https://multilaser.gupy.io"]),
    ("Centauro", "Varejo", "Gupy", ["https://centaurotalentos.gupy.io"]),
    ("Reserva", "Moda", "Gupy", ["https://reserva.gupy.io", "https://usereserva.gupy.io"]),
    ("V.tal", "Telecom", "Gupy", ["https://vtal.gupy.io"]),
    ("Ypê", "Varejo", "Gupy", ["https://carreirasype.gupy.io"]),
    ("C&A Brasil", "Varejo", "Gupy", ["https://cea.gupy.io"]),
    ("Grupo SBF", "Varejo", "Gupy", ["https://gruposbf.gupy.io", "https://centauro.gupy.io"]),
    ("Trackmob", "Tecnologia", "Gupy", ["https://trackmob.gupy.io"]),
    ("Cyrela", "Construção", "Gupy", ["https://cyrela.gupy.io"]),
    ("MRV", "Construção", "Gupy", ["https://mrv.gupy.io"]),
    ("Tramontina", "Indústria", "Gupy", ["https://tramontina.gupy.io"]),
    ("Grendene", "Indústria", "Gupy", ["https://grendene.gupy.io"]),
    ("Marfrig", "Alimentos e Bebidas", "Gupy", ["https://marfrig.gupy.io"]),
    ("Raízen", "Energia", "Gupy", ["https://genteraizen.gupy.io"]),
    ("Ultrapar", "Energia", "Gupy", ["https://ultrapar.gupy.io"]),
    ("Neoenergia", "Energia", "Gupy", ["https://carreiras.gupy.io/neoenergia"]),
    ("Copel", "Energia", "Gupy", ["https://copel.gupy.io"]),
    ("CPFL Energia", "Energia", "Gupy", ["https://cpflenergia.gupy.io"]),
    ("Eneva", "Energia", "Gupy", ["https://eneva.gupy.io"]),
    ("BRF", "Alimentos e Bebidas", "Gupy", ["https://brf.gupy.io"]),
    ("JBS", "Alimentos e Bebidas", "Gupy", ["https://grupojbs.gupy.io"]),
    ("Ambev", "Alimentos e Bebidas", "Gupy", ["https://ambev.gupy.io"]),
    ("Natura", "Cosméticos", "Gupy", ["https://natura.gupy.io", "https://avon.gupy.io"]),
    ("O Boticário", "Cosméticos", "Gupy", ["https://grupoboticario.gupy.io"]),
    ("Magazine Luiza", "Varejo", "Gupy", ["https://magazineluiza.gupy.io", "https://magalu.gupy.io"]),
    ("Americanas", "Varejo", "Gupy", ["https://americanas.gupy.io"]),
    ("Via Varejo", "Varejo", "Gupy", ["https://viavarejo.gupy.io", "https://grupocasasbahia.gupy.io"]),
    ("Carrefour Brasil", "Varejo", "Gupy", ["https://carrefour.gupy.io"]),
    ("Assaí", "Varejo", "Gupy", ["https://assai.gupy.io"]),
    ("Grupo Mateus", "Varejo", "Gupy", ["https://grupomateus.gupy.io"]),
    ("Havan", "Varejo", "Gupy", ["https://havan.gupy.io"]),
    ("Pernambucanas", "Varejo", "Gupy", ["https://pernambucanas.gupy.io"]),
    ("Riachuelo", "Varejo", "Gupy", ["https://riachuelo.gupy.io"]),
    ("Arezzo", "Varejo", "Gupy", ["https://arezzo.gupy.io", "https://azzas2154.gupy.io"]),
]


def detect_platform(url: str) -> str:
    u = url.lower()
    if ".gupy.io" in u:
        return "Gupy"
    if "greenhouse.io" in u:
        return "Greenhouse"
    if "inhire" in u:
        return "InHire"
    if "lever.co" in u:
        return "Lever"
    return "Site da Empresa"


def resolve_url(session, name: str, urls: list[str]) -> str | None:
    for url in urls:
        url = clean_url(url)
        if verify_website_status(session, url)["status"] == "1":
            return url
    found = _guesser.is_valid_ats(name)
    if found and verify_website_status(session, found)["status"] == "1":
        return clean_url(found)
    return None


def main():
    with open(LIST_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row.pop("Data de Publicação", None)

    existing_urls = {clean_url(r["URL"]) for r in rows}
    existing_names = {r["Nome da Empresa"].strip().lower() for r in rows}
    session = create_shared_session()
    today = date.today().strftime("%Y-%m-%d")
    added = 0

    for name, segment, _plat, urls in CANDIDATES:
        if name.strip().lower() in existing_names:
            continue
        url = resolve_url(session, name, urls)
        if not url or url in existing_urls:
            continue
        platform = detect_platform(url)
        rows.append(
            {
                "Status da URL": "1",
                "Data de Entrada": today,
                "Nome da Empresa": name,
                "Segmento da Empresa": to_macro(segment, name),
                "Plataforma": platform,
                "URL": url,
            }
        )
        existing_urls.add(url)
        existing_names.add(name.strip().lower())
        added += 1
        print(f"+ {name} -> {url}")

    with open(LIST_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Adicionadas {added} empresas (total {len(rows)})")


if __name__ == "__main__":
    main()
