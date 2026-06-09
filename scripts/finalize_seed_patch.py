#!/usr/bin/env python3
"""Consolida entradas verificadas e gera patch para known_career_urls.yaml."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT))

from scripts.scoring_utils import normalize_name
from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

YAML_PATH = ROOT / "data/seeds/known_career_urls.yaml"
LIST_PATH = ROOT / "src/data/input/list.csv"
BATCH_PATH = ROOT / "artifacts/known_career_urls_batch.yaml"
DISC_PATHS = [
    ROOT / "artifacts/discovery_url_unique.json",
    ROOT / "artifacts/discovered_urls.json",
    ROOT / "artifacts/discovered_urls_clean.json",
    ROOT / "artifacts/discovered_urls_pass2.json",
    ROOT / "artifacts/discovered_remaining.json",
    ROOT / "artifacts/curated_verified.json",
    ROOT / "artifacts/curated_extra_verified.json",
    ROOT / "artifacts/curated_batch_verified.json",
    ROOT / "artifacts/seed_sources_verified.json",
]
OUT_PATH = ROOT / "artifacts/known_career_urls_patch.yaml"

BAD_URL_FRAGMENTS = ("banco.gupy.io", "carreiras.gupy.io/", "portal.gupy.io", "vagas.gupy.io")

# Pesquisa web: slugs criativos / portais oficiais (B3, Valor 1000, Fortune BR)
WEB_RESEARCHED: list[tuple[str, str, list[str]]] = [
    ("Expresso São Miguel", "Logística e Mobilidade", ["https://sejaesm.gupy.io"]),
    ("Blue3 Investimentos", "Financeiro", ["https://vemserblue3.gupy.io"]),
    ("Fortbras", "Varejo e Consumo", ["https://fortbras.gupy.io"]),
    ("Grupo JCPM", "Mídia e Entretenimento", ["https://grupojcpm.gupy.io"]),
    ("MR3", "Logística e Mobilidade", ["https://mr3-operadorlogistico.gupy.io"]),
    ("Saint-Gobain Brasil", "Indústria", ["https://saintgobainbrasil.gupy.io"]),
    ("Veolia Brasil", "Energia e Utilities", ["https://carreirasveo.gupy.io"]),
    ("Mahindra Brasil", "Indústria", ["https://mahindra.gupy.io"]),
    ("CS Infra", "Construção e Imóveis", ["https://csinfra.gupy.io"]),
    ("ioasys", "Tecnologia", ["https://ioasys.gupy.io"]),
    ("Eucatex", "Indústria", ["https://eucatex.gupy.io"]),
    ("CoE Votorantim", "Indústria", ["https://votorantimcoe.gupy.io"]),
    ("Helbor", "Construção e Imóveis", ["https://helbor-hbr.gupy.io", "https://helbor.gupy.io"]),
    ("Banco BMG", "Financeiro", ["https://bmg.gupy.io"]),
    ("Banco Mercantil", "Financeiro", ["https://mercantil.gupy.io"]),
    ("Nio", "Energia e Utilities", ["https://nio.gupy.io"]),
    ("Hyva do Brasil", "Indústria", ["https://hyvadobrasil.gupy.io"]),
    ("KPMG Brasil", "Serviços e Outros", ["https://kpmgbrasil1.gupy.io"]),
    ("Deloitte Brasil", "Serviços e Outros", ["https://deloitte.gupy.io"]),
    ("EY Brasil", "Serviços e Outros", ["https://ey.gupy.io"]),
    ("McKinsey & Company", "Serviços e Outros", ["https://www.mckinsey.com/br/careers-in-brazil"]),
    ("Gympass", "Serviços e Outros", ["https://boards.greenhouse.io/gympass"]),
    ("Wellhub", "Serviços e Outros", ["https://boards.greenhouse.io/gympass"]),
    ("FGV", "Educação", ["https://portal.fgv.br/trabalhe-conosco"]),
    ("Netshoes", "Varejo e Consumo", ["https://jobs.kenoby.com/gruponetshoes"]),
    ("Banco Votorantim", "Financeiro", ["https://jobs.kenoby.com/bancobv"]),
    ("Dafiti Group", "Varejo e Consumo", ["https://dafiti.gupy.io"]),
    ("Grupo Carrefour Brasil", "Varejo e Consumo", ["https://grupocarrefourbrasil.gupy.io"]),
    ("Volkswagen do Brasil", "Indústria", ["https://vwbrasil.gupy.io"]),
    ("Claro", "Energia e Utilities", ["https://vempraclaro.gupy.io"]),
    ("Grupo Globo", "Mídia e Entretenimento", ["https://globo.gupy.io"]),
    ("Drogaria Araujo", "Saúde", ["https://drogaria.gupy.io"]),
    ("BoaVista SCPC", "Tecnologia", ["https://boavista.gupy.io"]),
    ("PagSeguro", "Tecnologia", ["https://pagseguro.gupy.io"]),
    ("Positivo Tecnologia", "Tecnologia", ["https://positivo.gupy.io"]),
    ("Azzas", "Varejo e Consumo", ["https://azzas2154.gupy.io"]),
    ("Farm Rio", "Varejo e Consumo", ["https://farm.gupy.io"]),
    ("Le Biscuit", "Varejo e Consumo", ["https://lebiscuit.gupy.io"]),
    ("Hering", "Varejo e Consumo", ["https://hering.gupy.io", "https://ciahering.gupy.io"]),
    ("Ypê", "Varejo e Consumo", ["https://carreirasype.gupy.io"]),
    ("Vibra Energia", "Energia e Utilities", ["https://vibraenergia.gupy.io"]),
    ("Orizon", "Energia e Utilities", ["https://orizon.gupy.io"]),
    ("Algar Telecom", "Energia e Utilities", ["https://algar.gupy.io"]),
    ("Brisanet", "Energia e Utilities", ["https://brisanet.gupy.io"]),
    ("Compass", "Energia e Utilities", ["https://compass.gupy.io"]),
    ("Vero Internet", "Energia e Utilities", ["https://vero.gupy.io"]),
    ("Aurora Alimentos", "Agro e Alimentos", ["https://auroracoop.gupy.io"]),
    ("Cocal", "Agro e Alimentos", ["https://cocal.gupy.io"]),
    ("Três Tentos", "Agro e Alimentos", ["https://3tentos.gupy.io"]),
    ("Ourofino", "Agro e Alimentos", ["https://ourofino.gupy.io"]),
    ("Plena Alimentos", "Agro e Alimentos", ["https://plena.gupy.io"]),
    ("Record", "Mídia e Entretenimento", ["https://recordtv.gupy.io"]),
    ("Tahto", "Serviços e Outros", ["https://tahto.gupy.io"]),
    ("Zamp", "Serviços e Outros", ["https://zamp.gupy.io"]),
    ("Valid", "Tecnologia", ["https://valid.gupy.io"]),
    ("Yduqs", "Educação", ["https://yduqs.gupy.io"]),
    ("Oficina do Estudante", "Educação", ["https://oficina.gupy.io"]),
    ("Afya", "Educação", ["https://afya.gupy.io"]),
    ("Aeris", "Indústria", ["https://aeris.gupy.io"]),
    ("BMW Brasil", "Indústria", ["https://bmw.gupy.io"]),
    ("Caoa Chery", "Indústria", ["https://caoa.gupy.io"]),
    ("Motiva", "Indústria", ["https://motiva.gupy.io"]),
    ("Randon", "Indústria", ["https://randoncorp.gupy.io"]),
    ("Scania Brasil", "Indústria", ["https://scania.gupy.io"]),
    ("Cyrela", "Construção e Imóveis", ["https://cyrela.gupy.io"]),
    ("Tempo Assist", "Saúde", ["https://tempo.gupy.io"]),
    ("Unimed Nacional", "Saúde", ["https://unimednacional.gupy.io"]),
    ("Bemobi", "Tecnologia", ["https://bemobi.gupy.io"]),
    ("Animale", "Varejo e Consumo", ["https://animale.gupy.io"]),
    ("Assaí", "Varejo e Consumo", ["https://assai.gupy.io"]),
    ("Americanas", "Varejo e Consumo", ["https://americanas.gupy.io"]),
    ("Via", "Varejo e Consumo", ["https://viavarejo.gupy.io"]),
    ("Vivara", "Varejo e Consumo", ["https://vivara.gupy.io"]),
    ("Lojas Renner", "Varejo e Consumo", ["https://lojasrenner.gupy.io"]),
    ("Itaú Unibanco", "Financeiro", ["https://vemproitau.gupy.io"]),
    ("Original", "Financeiro", ["https://original.gupy.io"]),
    ("Stone Co", "Financeiro", ["https://stone.gupy.io"]),
    ("Wiz", "Financeiro", ["https://wiz.gupy.io"]),
    ("Banco Guanabara", "Financeiro", ["https://guanabara.gupy.io"]),
    ("Banco Master", "Financeiro", ["https://master.gupy.io"]),
    ("SPX Capital", "Financeiro", ["https://spx.gupy.io"]),
    ("Western Union", "Financeiro", ["https://careers.westernunion.com"]),
    ("PwC", "Serviços e Outros", ["https://www.pwc.com.br/pt/carreira-na-pwc.html"]),
    ("Bain & Company", "Serviços e Outros", ["https://www.bain.com/careers"]),
    ("BCG", "Serviços e Outros", ["https://careers.bcg.com/global/en/locations/brazil"]),
    ("ManpowerGroup", "Serviços e Outros", ["https://www.manpowergroup.com/careers"]),
    ("CSU Cardsystem", "Serviços e Outros", ["https://csu.gupy.io"]),
    ("Atos", "Tecnologia", ["https://atos.net/en/careers"]),
    ("DXC Technology", "Tecnologia", ["https://careers.dxc.com"]),
    ("MongoDB", "Tecnologia", ["https://www.mongodb.com/careers"]),
    ("Palo Alto Networks", "Tecnologia", ["https://jobs.paloaltonetworks.com"]),
    ("Sinqia", "Tecnologia", ["https://jobs.quickin.io/sinqia/jobs"]),
    ("Snowflake", "Tecnologia", ["https://careers.snowflake.com"]),
    ("Stripe", "Tecnologia", ["https://stripe.com/jobs"]),
    ("Tata Consultancy Services", "Tecnologia", ["https://www.tcs.com/careers"]),
    ("Twilio", "Tecnologia", ["https://jobs.twilio.com"]),
    ("Unisys", "Tecnologia", ["https://www.unisys.com/careers"]),
    ("Wipro", "Tecnologia", ["https://careers.wipro.com"]),
    ("Kabum", "Varejo e Consumo", ["https://99jobs.com/kabum/jobs"]),
    ("EF Education First", "Educação", ["https://careers.ef.com"]),
    ("Disney Brasil", "Mídia e Entretenimento", ["https://jobs.disneycareers.com"]),
    ("Banco Bari", "Financeiro", ["https://bari.gupy.io"]),
    ("Banco BMP", "Financeiro", ["https://bmp.gupy.io"]),
    ("Banco Bocom BBM", "Financeiro", ["https://bocom.gupy.io"]),
    ("Banco Cetelem", "Financeiro", ["https://cetelem.gupy.io"]),
    ("Banco Cifra", "Financeiro", ["https://cifra.gupy.io"]),
    ("Banco Digimais", "Financeiro", ["https://digimais.gupy.io"]),
    ("Banco Olé Bonsucesso", "Financeiro", ["https://ole.gupy.io"]),
    ("Banco Plural", "Financeiro", ["https://brasilplural.gupy.io"]),
    ("Expresso Nepomuceno", "Logística e Mobilidade", ["https://en.gupy.io"]),
    ("Bemol", "Varejo e Consumo", ["https://bemol.gupy.io"]),
    ("Realize", "Financeiro", ["https://realize.gupy.io"]),
    ("Repassa", "Varejo e Consumo", ["https://repassa.gupy.io"]),
    ("Portobello Shop", "Varejo e Consumo", ["https://portobelloshop.gupy.io"]),
    ("Even", "Construção e Imóveis", ["https://sejaeven.gupy.io"]),
    ("Banco Daycoval", "Financeiro", ["https://bancodaycoval.gupy.io"]),
    ("Banco Sofisa", "Financeiro", ["https://bancosofisa.gupy.io"]),
    ("Banco Fibra", "Financeiro", ["https://bancofibra.gupy.io"]),
    ("Rodobens", "Financeiro", ["https://rodobenscarreiras.gupy.io"]),
    ("Mitre Realty", "Construção e Imóveis", ["https://mitrerealty.gupy.io"]),
    ("Uello", "Logística e Mobilidade", ["https://uello.gupy.io"]),
    ("Log-In Logística", "Logística e Mobilidade", ["https://loginlogistica.gupy.io"]),
    ("Rumo", "Logística e Mobilidade", ["https://rumolog.gupy.io"]),
    ("LOG Commercial Properties", "Construção e Imóveis", ["https://logcp.gupy.io"]),
    ("Track&Field", "Varejo e Consumo", ["https://tfcarreira.gupy.io"]),
    ("RSM Brasil", "Serviços e Outros", ["https://rsmbrasil.gupy.io"]),
    ("Encantech", "Tecnologia", ["https://encantech.gupy.io"]),
    ("Grupo Petz", "Varejo e Consumo", ["https://petz.gupy.io"]),
    ("Riachuelo", "Varejo e Consumo", ["https://riachuelo.gupy.io"]),
    ("Decathlon Brasil", "Varejo e Consumo", ["https://carreirasdecathlon.gupy.io"]),
    ("Cobasi", "Varejo e Consumo", ["https://cobasi.pandape.infojobs.com.br"]),
    ("Tok&Stok", "Varejo e Consumo", ["https://tokstok.pandape.infojobs.com.br"]),
    ("Centauro", "Varejo e Consumo", ["https://centaurotalentos.gupy.io"]),
    ("Grupo SBF", "Varejo e Consumo", ["https://gruposbf.gupy.io"]),
    ("Intelbras", "Tecnologia", ["https://intelbras.gupy.io"]),
    ("Senior Sistemas", "Tecnologia", ["https://senior.gupy.io"]),
    ("Locaweb", "Tecnologia", ["https://locaweb.gupy.io"]),
    ("Stefanini", "Tecnologia", ["https://stefanini.gupy.io"]),
    ("TOTVS", "Tecnologia", ["https://carreiras.gupy.io/totvs"]),
    ("Linx", "Tecnologia", ["https://carreiras.gupy.io/linx"]),
    ("CI&T", "Tecnologia", ["https://ciandt.gupy.io"]),
    ("Boa Vista Serviços", "Serviços e Outros", ["https://boavista.gupy.io"]),
    ("Serasa", "Serviços e Outros", ["https://serasa.gupy.io"]),
    ("Equifax Brasil", "Serviços e Outros", ["https://equifax.gupy.io"]),
    ("StoneCo", "Financeiro", ["https://stone.gupy.io"]),
    ("C6 Bank", "Financeiro", ["https://boards.greenhouse.io/c6bank"]),
    ("Creditas", "Financeiro", ["https://creditas.gupy.io"]),
    ("Neon", "Financeiro", ["https://jobs.lever.co/neon"]),
    ("Will Bank", "Financeiro", ["https://willbank.inhire.app/vagas"]),
    ("Agibank", "Financeiro", ["https://job-boards.greenhouse.io/agibank"]),
    ("Banrisul", "Financeiro", ["https://banrisul.gupy.io"]),
    ("Banestes", "Financeiro", ["https://carreiras.gupy.io/banestes"]),
    ("Banco Rendimento", "Financeiro", ["https://carreiras.gupy.io/bancorendimento"]),
    ("Banco Topázio", "Financeiro", ["https://bancotopazio.gupy.io"]),
    ("Banco Pan", "Financeiro", ["https://bancopan.gupy.io"]),
    ("Paraná Banco", "Financeiro", ["https://paranabanco.gupy.io"]),
    ("Banco BS2", "Financeiro", ["https://bs2.gupy.io"]),
    ("Omni", "Financeiro", ["https://omni.gupy.io"]),
    ("Crefisa", "Financeiro", ["https://crefisa.gupy.io"]),
    ("Banco Modal", "Financeiro", ["https://modal.gupy.io"]),
    ("Alelo", "Financeiro", ["https://alelo.inhire.app/vagas"]),
    ("Ticket", "Financeiro", ["https://carreiras.gupy.io/edenred"]),
    ("Pluxee", "Financeiro", ["https://pluxee.gupy.io"]),
    ("Getnet", "Financeiro", ["https://carreiras.gupy.io/getnet"]),
    ("Cielo", "Financeiro", ["https://cielo.gupy.io"]),
    ("Rede", "Financeiro", ["https://rede.gupy.io"]),
    ("PicPay", "Financeiro", ["https://carreiras.gupy.io/picpay"]),
    ("Mercado Pago", "Financeiro", ["https://mercadopago.gupy.io"]),
    ("PagBank", "Financeiro", ["https://carreiras.gupy.io/pagbank"]),
    ("SumUp", "Financeiro", ["https://boards.greenhouse.io/sumup"]),
    ("Clear", "Financeiro", ["https://boards.greenhouse.io/clear"]),
    ("XP Inc", "Financeiro", ["https://boards.greenhouse.io/xpinc"]),
    ("BTG Pactual", "Financeiro", ["https://boards.greenhouse.io/btgpactual"]),
    ("Inter", "Financeiro", ["https://boards.greenhouse.io/inter"]),
    ("Nubank", "Financeiro", ["https://boards.greenhouse.io/nubank"]),
    ("Banco BMG", "Financeiro", ["https://bmg.gupy.io"]),
    ("Banco Mercantil", "Financeiro", ["https://mercantil.gupy.io"]),
    ("Banco Industrial do Brasil", "Financeiro", ["https://bib.gupy.io"]),
    ("Sinqia", "Tecnologia", ["https://jobs.quickin.io/sinqia/jobs"]),
    ("Tenda", "Construção e Imóveis", ["https://tenda.gupy.io"]),
    ("MRV", "Construção e Imóveis", ["https://carreiras.gupy.io/mrv"]),
    ("Eztec", "Construção e Imóveis", ["https://eztec.gupy.io"]),
    ("JHSF", "Construção e Imóveis", ["https://jhsf.gupy.io"]),
    ("Multiplan", "Varejo e Consumo", ["https://multiplan.gupy.io"]),
    ("Iguatemi", "Varejo e Consumo", ["https://iguatemi.gupy.io"]),
    ("Aliansce Sonae", "Varejo e Consumo", ["https://alianscesonae.gupy.io"]),
    ("BrMalls", "Varejo e Consumo", ["https://carreirasallos.gupy.io"]),
    ("Atacadão", "Varejo e Consumo", ["https://carreiras.gupy.io/atacadao"]),
    ("Grupo Mateus", "Varejo e Consumo", ["https://carreiras.gupy.io/grupomateus"]),
    ("GPA", "Varejo e Consumo", ["https://gpabr.gupy.io"]),
    ("Casas Bahia", "Varejo e Consumo", ["https://grupocasasbahia.gupy.io"]),
    ("Magazine Luiza", "Varejo e Consumo", ["https://magazineluiza.inhire.app/vagas"]),
    ("Havan", "Varejo e Consumo", ["https://carreiras.gupy.io/havan"]),
    ("Riachuelo", "Varejo e Consumo", ["https://riachuelo.gupy.io"]),
    ("Marisa", "Varejo e Consumo", ["https://carreiras.gupy.io/marisa"]),
    ("Pernambucanas", "Varejo e Consumo", ["https://pernambucanas.gupy.io"]),
    ("Arezzo", "Varejo e Consumo", ["https://azzas2154.gupy.io"]),
    ("Grupo Soma", "Varejo e Consumo", ["https://gruposoma.gupy.io"]),
    ("Alpargatas", "Varejo e Consumo", ["https://alpargatas.gupy.io"]),
    ("Natura", "Varejo e Consumo", ["https://natura.gupy.io"]),
    ("Boticário", "Varejo e Consumo", ["https://grupoboticario.gupy.io"]),
    ("Raia Drogasil", "Saúde", ["https://carreiras.gupy.io/rd"]),
    ("Rede D'Or", "Saúde", ["https://rededor.gupy.io"]),
    ("Dasa", "Saúde", ["https://carreiras.gupy.io/dasa"]),
    ("Einstein", "Saúde", ["https://einstein.gupy.io"]),
    ("Fleury", "Saúde", ["https://grupofleury.gupy.io"]),
    ("Eurofarma", "Saúde", ["https://eurofarma.gupy.io"]),
    ("Aché", "Saúde", ["https://vagasache.gupy.io"]),
    ("Hypera", "Saúde", ["https://carreiras.gupy.io/hypera"]),
    ("EMS", "Saúde", ["https://ems.izirh.io"]),
    ("Klabin", "Indústria", ["https://klabin.inhire.app/vagas"]),
    ("Suzano", "Indústria", ["https://suzano.gupy.io"]),
    ("Gerdau", "Indústria", ["https://career19.sapsf.com/careers?company=gerdauacos"]),
    ("Usiminas", "Indústria", ["https://usiminas.gupy.io"]),
    ("CSN", "Indústria", ["https://csn.gupy.io"]),
    ("Grendene", "Indústria", ["https://carreiras.gupy.io/grendene"]),
    ("Marcopolo", "Indústria", ["https://marcopolo.gupy.io"]),
    ("Embraer", "Indústria", ["https://embraer.gupy.io"]),
    ("WEG", "Indústria", ["https://weg.gupy.io"]),
    ("Tupy", "Indústria", ["https://tupy.gupy.io"]),
    ("Raízen", "Energia e Utilities", ["https://genteraizen.gupy.io"]),
    ("Vibra Energia", "Energia e Utilities", ["https://vibraenergia.gupy.io"]),
    ("Ipiranga", "Energia e Utilities", ["https://ipiranga.gupy.io"]),
    ("Equatorial", "Energia e Utilities", ["https://equatorialenergia.gupy.io"]),
    ("Neoenergia", "Energia e Utilities", ["https://carreiras.gupy.io/neoenergia"]),
    ("Copel", "Energia e Utilities", ["https://carreiras.gupy.io/copel"]),
    ("CPFL Energia", "Energia e Utilities", ["https://carreiras.gupy.io/cpfl"]),
    ("Eneva", "Energia e Utilities", ["https://carreiras.gupy.io/eneva"]),
    ("AES Brasil", "Energia e Utilities", ["https://carreiras.gupy.io/aes"]),
    ("Engie Brasil", "Energia e Utilities", ["https://jobs.engie.com"]),
    ("EDP Brasil", "Energia e Utilities", ["https://jobs.edp.com"]),
    ("JBS", "Agro e Alimentos", ["https://grupojbs.gupy.io"]),
    ("Marfrig", "Agro e Alimentos", ["https://marfrig.gupy.io"]),
    ("BRF", "Agro e Alimentos", ["https://carreiras.gupy.io/brf"]),
    ("Minerva", "Agro e Alimentos", ["https://minervafoods.gupy.io"]),
    ("Ambev", "Agro e Alimentos", ["https://ambev.gupy.io"]),
    ("Copersucar", "Agro e Alimentos", ["https://copersucar.gupy.io"]),
    ("SLC Agrícola", "Agro e Alimentos", ["https://slcagricola.gupy.io"]),
    ("Bauducco", "Agro e Alimentos", ["https://bauducco.gupy.io"]),
    ("Piracanjuba", "Agro e Alimentos", ["https://piracanjuba.gupy.io"]),
    ("Camil", "Agro e Alimentos", ["https://platform.senior.com.br/hcmrs/hcm/curriculo/?tenant=camilcombr"]),
    ("Azul", "Logística e Mobilidade", ["https://voeazul.gupy.io"]),
    ("GOL", "Logística e Mobilidade", ["https://gol.gupy.io"]),
    ("LATAM Airlines", "Logística e Mobilidade", ["https://latam.gupy.io"]),
    ("Localiza", "Logística e Mobilidade", ["https://localiza.gupy.io"]),
    ("Movida", "Logística e Mobilidade", ["https://movida.gupy.io"]),
    ("Unidas", "Logística e Mobilidade", ["https://unidas.gupy.io"]),
    ("CCR", "Logística e Mobilidade", ["https://ccr.gupy.io"]),
    ("VLI", "Logística e Mobilidade", ["https://vli-logistica.gupy.io"]),
    ("JSL", "Logística e Mobilidade", ["https://jsl.gupy.io"]),
    ("Total Express", "Logística e Mobilidade", ["https://totalexpress.gupy.io"]),
    ("Correios", "Logística e Mobilidade", ["https://correios.gupy.io"]),
    ("Yduqs", "Educação", ["https://yduqs.gupy.io"]),
    ("Cogna", "Educação", ["https://cogna.gupy.io"]),
    ("Anima", "Educação", ["https://anima.gupy.io"]),
    ("Grupo Salta", "Educação", ["https://carreiras.gupy.io/salta"]),
    ("Estácio", "Educação", ["https://estacio.gupy.io"]),
    ("Kroton", "Educação", ["https://kroton.gupy.io"]),
    ("Globo", "Mídia e Entretenimento", ["https://globo.gupy.io"]),
    ("Band", "Mídia e Entretenimento", ["https://band.jobs.recrut.ai/#openings"]),
    ("UOL", "Mídia e Entretenimento", ["https://uol.gupy.io"]),
    ("Wildlife", "Mídia e Entretenimento", ["https://boards.greenhouse.io/wildlifestudios"]),
    ("iFood", "Tecnologia", ["https://carreiras.ifood.com.br"]),
    ("Mercado Livre", "Tecnologia", ["https://mercadolibre.gupy.io"]),
    ("VTEX", "Tecnologia", ["https://job-boards.greenhouse.io/vtex"]),
    ("RD Station", "Tecnologia", ["https://boards.greenhouse.io/rdstation"]),
    ("Loggi", "Tecnologia", ["https://carreiras.gupy.io/loggi"]),
    ("QuintoAndar", "Construção e Imóveis", ["https://boards.greenhouse.io/quintoandar"]),
]


def url_key(url: str) -> tuple:
    u = clean_url(url).lower().rstrip("/")
    p = urlparse(u)
    host = p.netloc.replace("www.", "")
    path = p.path.rstrip("/")
    if host.endswith(".gupy.io") and host not in ("carreiras.gupy.io", "portal.gupy.io"):
        return ("gupy", host.split(".")[0])
    if "carreiras.gupy.io" in host and path:
        return ("gupy", path.strip("/").split("/")[0])
    if "greenhouse.io" in host:
        parts = [x for x in path.split("/") if x]
        return ("gh", parts[-1] if parts else host)
    return ("full", u)


def is_bad_url(url: str) -> bool:
    u = url.lower()
    return any(b in u for b in BAD_URL_FRAGMENTS)


def load_excluded_names() -> set[str]:
    names: set[str] = set()
    for c in yaml.safe_load(YAML_PATH.read_text(encoding="utf-8")).get("companies", []):
        names.add(normalize_name(c["name"]))
    with open(LIST_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(normalize_name(row["Nome da Empresa"]))
    return names


def parse_batch_yaml(text: str) -> list[tuple[str, str, list[str]]]:
    out = []
    for m in re.finditer(
        r"- name: (.+)\n  macro: (.+)\n  urls:\n((?:  - .+\n)+)", text
    ):
        name, macro, urls_block = m.groups()
        urls = [u.strip()[2:] for u in urls_block.strip().split("\n")]
        out.append((name, macro, urls))
    return out


def collect_candidates() -> list[tuple[str, str, list[str]]]:
    items: list[tuple[str, str, list[str]]] = []
    items.extend(WEB_RESEARCHED)
    if BATCH_PATH.exists():
        items.extend(parse_batch_yaml(BATCH_PATH.read_text(encoding="utf-8")))
    for disc_path in DISC_PATHS:
        if not disc_path.exists():
            continue
        for d in json.loads(disc_path.read_text(encoding="utf-8")):
            items.append((d["name"], d["macro"], d["urls"]))
    return items


def verify_entry(name: str, macro: str, urls: list[str], session) -> dict | None:
    for url in urls:
        if is_bad_url(url):
            continue
        url = clean_url(url)
        if verify_website_status(session, url)["status"] != "1":
            continue
        if not verify_portal_has_jobs(url, session):
            continue
        good = [url]
        for u in urls:
            u = clean_url(u)
            if u != url and not is_bad_url(u):
                good.append(u)
            if len(good) >= 3:
                break
        return {"name": name.strip(), "macro": macro, "urls": good[:3]}
    return None


def render_yaml(entries: list[dict]) -> str:
    by_macro: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_macro[e["macro"]].append(e)
    order = [
        "Financeiro",
        "Tecnologia",
        "Varejo e Consumo",
        "Saúde",
        "Indústria",
        "Energia e Utilities",
        "Logística e Mobilidade",
        "Construção e Imóveis",
        "Educação",
        "Agro e Alimentos",
        "Mídia e Entretenimento",
        "Serviços e Outros",
    ]
    lines = [
        "# === Lote curado: B3 + Valor 1000 + Multinacionais BR ===",
        "# Fonte: B3 (jun/2026), Valor 1000 (ed. 2025), Fortune Global 500",
        "",
    ]
    for macro in order:
        items = by_macro.get(macro, [])
        if not items:
            continue
        lines.append(f"# --- {macro} ---")
        for item in sorted(items, key=lambda x: x["name"].lower()):
            lines.append(f"- name: {item['name']}")
            lines.append(f"  macro: {macro}")
            lines.append("  urls:")
            for url in item["urls"]:
                lines.append(f"  - {url}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    excluded_names = load_excluded_names()
    session = create_shared_session()
    seen_names: set[str] = set()
    seen_keys: set[tuple] = set()
    verified: list[dict] = []

    for name, macro, urls in collect_candidates():
        nkey = normalize_name(name)
        if nkey in excluded_names or nkey in seen_names:
            continue
        urls = [u for u in urls if not is_bad_url(u)]
        if not urls:
            continue

        entry = verify_entry(name, macro, urls, session)
        if not entry:
            continue
        k = url_key(entry["urls"][0])
        if k in seen_keys:
            continue
        seen_keys.add(k)
        seen_names.add(nkey)
        verified.append(entry)
        print(f"+ {entry['name']} -> {entry['urls'][0]}")

    patch = render_yaml(verified)
    OUT_PATH.write_text(patch, encoding="utf-8")
    print(f"\nVerificadas: {len(verified)}")
    print(f"Patch -> {OUT_PATH}")


if __name__ == "__main__":
    main()
