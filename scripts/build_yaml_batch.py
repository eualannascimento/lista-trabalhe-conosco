#!/usr/bin/env python3
"""Monta lote YAML a partir de URLs verificadas e descobertas."""

import csv
import json
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from unidecode import unidecode

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.py.functions.df_operations import clean_url
from src.py.functions.portal_verification import verify_portal_has_jobs
from src.py.functions.website_verification import create_shared_session, verify_website_status

YAML_PATH = ROOT / "data/seeds/known_career_urls.yaml"
LIST_PATH = ROOT / "src/data/input/list.csv"
OUT_PATH = ROOT / "artifacts/known_career_urls_batch.yaml"

# Lote curado: B3 + Valor 1000 + Fortune BR (URLs pesquisadas/verificadas)
BATCH: list[tuple[str, str, list[str]]] = [
    # Financeiro
    ("McKinsey & Company", "Financeiro", ["https://www.mckinsey.com/br/careers-in-brazil"]),
    ("BCG", "Financeiro", ["https://careers.bcg.com/global/en/locations/brazil"]),
    ("Bain & Company", "Financeiro", ["https://www.bain.com/careers/"]),
    ("PwC", "Financeiro", ["https://www.pwc.com.br/pt/carreira-na-pwc.html"]),
    ("Marsh", "Financeiro", ["https://careers.marsh.com"]),
    ("Mercer", "Financeiro", ["https://careers.mercer.com"]),
    ("ManpowerGroup", "Financeiro", ["https://www.manpowergroup.com.br/candidatos"]),
    ("Randstad Brasil", "Financeiro", ["https://www.randstad.com.br"]),
    ("ISS Brasil", "Financeiro", ["https://jobs.issworld.com"]),
    ("Toro Investimentos", "Financeiro", ["https://toroinvestimentos.gupy.io"]),
    ("Órama", "Financeiro", ["https://orama.gupy.io"]),
    ("Rico", "Financeiro", ["https://rico.gupy.io"]),
    ("IRB Brasil RE", "Financeiro", ["https://irbre.gupy.io"]),
    ("Pátria Investimentos", "Financeiro", ["https://patria.gupy.io"]),
    ("BR Partners", "Financeiro", ["https://brpartners.gupy.io"]),
    ("Adam Capital", "Financeiro", ["https://adamcapital.gupy.io"]),
    ("Verde Asset", "Financeiro", ["https://verdeasset.gupy.io"]),
    ("SPX Capital", "Financeiro", ["https://spxcapital.gupy.io"]),
    ("ARX", "Financeiro", ["https://arxinvestimentos.gupy.io"]),
    ("Bozano Investimentos", "Financeiro", ["https://bozano.gupy.io"]),
    ("Wright Capital", "Financeiro", ["https://wrightcapital.gupy.io"]),
    ("Kapitalo", "Financeiro", ["https://kapitalo.gupy.io"]),
    ("Garde", "Financeiro", ["https://garde.gupy.io"]),
    ("Ibiuna", "Financeiro", ["https://ibiuna.gupy.io"]),
    ("Legacy Capital", "Financeiro", ["https://legacycapital.gupy.io"]),
    ("Dynamo", "Financeiro", ["https://dynamo.gupy.io"]),
    ("Atmos Capital", "Financeiro", ["https://atmoscapital.gupy.io"]),
    ("Truxt", "Financeiro", ["https://truxt.gupy.io"]),
    ("Mosaico", "Financeiro", ["https://mosaico.gupy.io"]),
    ("Avenue", "Financeiro", ["https://avenue.gupy.io"]),
    ("Empiricus", "Financeiro", ["https://empiricus.gupy.io"]),
    ("Suno Research", "Financeiro", ["https://suno.gupy.io"]),
    ("StatusInvest", "Financeiro", ["https://statusinvest.gupy.io"]),
    ("Capital Aberto", "Financeiro", ["https://capitalaberto.gupy.io"]),
    ("Easynvest", "Financeiro", ["https://easynvest.gupy.io"]),
    ("XP Investimentos", "Financeiro", ["https://boards.greenhouse.io/xpinc"]),
    ("Hipercard", "Financeiro", ["https://hipercard.gupy.io"]),
    ("Wise", "Financeiro", ["https://wise.jobs"]),
    ("Remessa Online", "Financeiro", ["https://remessaonline.gupy.io"]),
    ("MoneyGram", "Financeiro", ["https://corporate.moneygram.com/careers"]),
    ("Western Union", "Financeiro", ["https://careers.westernunion.com"]),
    ("FinanZero", "Financeiro", ["https://finanzero.gupy.io"]),
    ("Acordo Certo", "Financeiro", ["https://acordocerto.gupy.io"]),
    ("Quero Quitar", "Financeiro", ["https://queroquitar.gupy.io"]),
    ("Konkero", "Financeiro", ["https://konkero.gupy.io"]),
    ("Biva", "Financeiro", ["https://biva.gupy.io"]),
    ("Bcredi", "Financeiro", ["https://bcredi.gupy.io"]),
    ("Provu", "Financeiro", ["https://provu.gupy.io"]),
    ("Just", "Financeiro", ["https://just.gupy.io"]),
    ("Kavod Lending", "Financeiro", ["https://kavod.gupy.io"]),
    ("BHub", "Financeiro", ["https://bhub.gupy.io"]),
    ("Nibo", "Financeiro", ["https://nibo.gupy.io"]),
    ("Banco Master", "Financeiro", ["https://master.gupy.io"]),
    ("Itaú Unibanco", "Financeiro", ["https://vemproitau.gupy.io"]),
    ("Original", "Financeiro", ["https://original.gupy.io"]),
    ("Stone Co", "Financeiro", ["https://stone.gupy.io"]),
    ("Sumup", "Financeiro", ["https://boards.greenhouse.io/sumup"]),
    ("Banco Rendimento", "Financeiro", ["https://rendimento.gupy.io"]),
    ("Banco Rodobens", "Financeiro", ["https://rodobens.gupy.io"]),
    ("Banco Guanabara", "Financeiro", ["https://guanabara.gupy.io"]),
    ("Banco Paulista", "Financeiro", ["https://paulista.gupy.io"]),
    ("Banco Semear", "Financeiro", ["https://semear.gupy.io"]),
    ("Banco Topázio", "Financeiro", ["https://topazio.gupy.io"]),
    ("Banco Pine", "Financeiro", ["https://bancopine.gupy.io"]),
    ("Banco Fibra", "Financeiro", ["https://fibra.gupy.io"]),
    ("Banco BMP", "Financeiro", ["https://bmp.gupy.io"]),
    ("Banco Digimais", "Financeiro", ["https://digimais.gupy.io"]),
    ("Banco da China Brasil", "Financeiro", ["https://bankofchina.gupy.io"]),
    ("Banco Rabobank International Brasil", "Financeiro", ["https://rabobank.gupy.io"]),
    ("Sumitomo Mitsui", "Financeiro", ["https://sumitomo.gupy.io"]),
    ("MUFG Brasil", "Financeiro", ["https://mufg.gupy.io"]),
    ("Mizuho", "Financeiro", ["https://mizuho.gupy.io"]),
    ("Scotiabank", "Financeiro", ["https://scotiabank.gupy.io"]),
    ("Deutsche Bank", "Financeiro", ["https://careers.db.com"]),
    ("Citibank Brasil", "Financeiro", ["https://jobs.citi.com"]),
    ("Morgan Stanley", "Financeiro", ["https://morganstanley.eightfold.ai/careers"]),
    ("Goldman Sachs", "Financeiro", ["https://hdpc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CampusHiring"]),
    ("JP Morgan", "Financeiro", ["https://careers.jpmorgan.com"]),
    ("Credit Suisse", "Financeiro", ["https://careers.ubs.com"]),
    ("UBS BB", "Financeiro", ["https://careers.ubs.com"]),
    ("HSBC Brasil", "Financeiro", ["https://mycareer.hsbc.com"]),
    ("Banese", "Financeiro", ["https://banese.gupy.io"]),
    ("Banpará", "Financeiro", ["https://banpara.gupy.io"]),
    ("BNDES", "Financeiro", ["https://www.bndes.gov.br/wps/portal/site/home/transparencia/concursos-e-selecoes"]),
    ("Bradesco Saúde", "Financeiro", ["https://bradescosaude.gupy.io"]),
    ("Itaú BBA", "Financeiro", ["https://itau-bba.gupy.io"]),
    ("Brasilcap", "Financeiro", ["https://brasilcap.gupy.io"]),
    ("Chubb", "Financeiro", ["https://chubb.com/br-pt/careers.html"]),
    ("AIG", "Financeiro", ["https://www.aig.com/home/careers"]),
    ("Willis Towers Watson", "Financeiro", ["https://careers.wtwco.com"]),
    ("Cetelem", "Financeiro", ["https://cetelem.gupy.io"]),
    ("Santander Consumer", "Financeiro", ["https://santanderconsumer.gupy.io"]),
    ("Renner Card", "Financeiro", ["https://rennercard.gupy.io"]),
    ("Banco Olé", "Financeiro", ["https://oleconsignado.gupy.io"]),
    ("Ticket", "Financeiro", ["https://carreiras.gupy.io/edenred"]),
    ("Edenred", "Financeiro", ["https://pluxee.gupy.io"]),
    # Tecnologia
    ("Sinqia", "Tecnologia", ["https://jobs.quickin.io/sinqia/jobs"]),
    ("Stripe", "Tecnologia", ["https://stripe.com/jobs"]),
    ("Twilio", "Tecnologia", ["https://jobs.twilio.com"]),
    ("GitLab", "Tecnologia", ["https://about.gitlab.com/jobs"]),
    ("MongoDB", "Tecnologia", ["https://www.mongodb.com/careers"]),
    ("Snowflake", "Tecnologia", ["https://careers.snowflake.com"]),
    ("Cloudflare", "Tecnologia", ["https://www.cloudflare.com/careers"]),
    ("Palo Alto Networks", "Tecnologia", ["https://jobs.paloaltonetworks.com"]),
    ("VMware", "Tecnologia", ["https://careers.vmware.com"]),
    ("Red Hat", "Tecnologia", ["https://redhat.wd5.myworkdayjobs.com"]),
    ("Cognizant", "Tecnologia", ["https://careers.cognizant.com"]),
    ("Wipro", "Tecnologia", ["https://careers.wipro.com"]),
    ("TCS", "Tecnologia", ["https://www.tcs.com/careers"]),
    ("Globant", "Tecnologia", ["https://careers.globant.com"]),
    ("EPAM", "Tecnologia", ["https://www.epam.com/careers"]),
    ("DXC Technology", "Tecnologia", ["https://careers.dxc.com"]),
    ("Atos", "Tecnologia", ["https://atos.net/en/careers"]),
    ("Unisys", "Tecnologia", ["https://www.unisys.com/careers"]),
    ("Indra Brasil", "Tecnologia", ["https://www.indracompany.com/careers"]),
    ("Sonda Brasil", "Tecnologia", ["https://sonda.gupy.io"]),
    ("Politec", "Tecnologia", ["https://politec.gupy.io"]),
    ("Idwall", "Tecnologia", ["https://idwall.gupy.io"]),
    ("Eduzz", "Tecnologia", ["https://eduzz.gupy.io"]),
    ("Gympass", "Tecnologia", ["https://boards.greenhouse.io/gympass"]),
    ("Wellhub", "Tecnologia", ["https://boards.greenhouse.io/gympass"]),
    # Varejo e Consumo
    ("Dafiti", "Varejo e Consumo", ["https://dafiti.gupy.io"]),
    ("Netshoes", "Varejo e Consumo", ["https://jobs.kenoby.com/gruponetshoes"]),
    ("Kabum", "Varejo e Consumo", ["https://99jobs.com/kabum/jobs"]),
    ("KaBuM", "Varejo e Consumo", ["https://99jobs.com/kabum/jobs"]),
    ("Colombo", "Varejo e Consumo", ["https://colombo.gupy.io"]),
    ("Osklen", "Varejo e Consumo", ["https://osklen.gupy.io"]),
    ("Animale", "Varejo e Consumo", ["https://animale.gupy.io"]),
    ("Farm Rio", "Varejo e Consumo", ["https://farmrio.gupy.io"]),
    ("Schutz", "Varejo e Consumo", ["https://schutz.gupy.io"]),
    ("Malwee", "Varejo e Consumo", ["https://malwee.gupy.io"]),
    ("Lupo", "Varejo e Consumo", ["https://lupo.gupy.io"]),
    ("Melissa", "Varejo e Consumo", ["https://melissa.gupy.io"]),
    ("Olympikus", "Varejo e Consumo", ["https://olympikus.gupy.io"]),
    ("Eudora", "Varejo e Consumo", ["https://eudora.gupy.io"]),
    ("Colgate", "Varejo e Consumo", ["https://colgatepalmolive.gupy.io"]),
    ("Henkel", "Varejo e Consumo", ["https://henkel.gupy.io"]),
    ("Bombril", "Varejo e Consumo", ["https://bombril.gupy.io"]),
    ("Grupo Petrópolis", "Varejo e Consumo", ["https://petropolis.gupy.io"]),
    ("Pernod Ricard", "Varejo e Consumo", ["https://pernodricard.gupy.io"]),
    ("Lactalis", "Varejo e Consumo", ["https://lactalis.gupy.io"]),
    ("Vigor", "Varejo e Consumo", ["https://vigor.gupy.io"]),
    ("Tirol Laticínios", "Varejo e Consumo", ["https://tirol.gupy.io"]),
    ("Grupo Carrefour Brasil", "Varejo e Consumo", ["https://grupocarrefourbrasil.gupy.io"]),
    ("Maria Filó", "Varejo e Consumo", ["https://mariafilo.gupy.io"]),
    # Saúde
    ("Aurora Alimentos", "Saúde", ["https://aurora.gupy.io"]),
    ("Vetnil", "Saúde", ["https://vetnil.gupy.io"]),
    ("Mantecorp", "Saúde", ["https://mantecorp.gupy.io"]),
    ("Apsen", "Saúde", ["https://apsen.gupy.io"]),
    ("Geolab", "Saúde", ["https://geolab.gupy.io"]),
    ("Sandoz", "Saúde", ["https://sandoz.gupy.io"]),
    ("Galena", "Saúde", ["https://galena.gupy.io"]),
    ("MV Sistemas", "Saúde", ["https://mvsistemas.gupy.io"]),
    ("Pixeon", "Saúde", ["https://pixeon.gupy.io"]),
    ("Zenklub", "Saúde", ["https://zenklub.gupy.io"]),
    ("Panvel", "Saúde", ["https://panvel.gupy.io"]),
    ("Drogaria Araujo", "Saúde", ["https://araujo.gupy.io"]),
    ("Profarma", "Saúde", ["https://profarma.gupy.io"]),
    ("Mater Dei", "Saúde", ["https://materdei.gupy.io"]),
    ("Oncoclínicas", "Saúde", ["https://oncoclinicas.gupy.io"]),
    ("Hermes Pardini", "Saúde", ["https://hermespardini.gupy.io"]),
    ("Unimed Brasil", "Saúde", ["https://unimed.gupy.io"]),
    # Indústria
    ("Volkswagen do Brasil", "Indústria", ["https://vwbrasil.gupy.io"]),
    ("Mercedes-Benz Brasil", "Indústria", ["https://mercedes-benz.gupy.io"]),
    ("Votorantim Cimentos", "Indústria", ["https://votorantimcimentos.gupy.io"]),
    ("CoE Votorantim", "Indústria", ["https://votorantimcoe.gupy.io"]),
    ("Iochpe-Maxion", "Indústria", ["https://maxion.gupy.io"]),
    ("Romi", "Indústria", ["https://romi.gupy.io"]),
    ("Fras-le", "Indústria", ["https://frasle.gupy.io"]),
    ("Schulz", "Indústria", ["https://schulz.gupy.io"]),
    ("Atech", "Indústria", ["https://atech.gupy.io"]),
    ("Avibras", "Indústria", ["https://avibras.gupy.io"]),
    ("Helibras", "Indústria", ["https://helicopteros.gupy.io"]),
    ("Caoa Chery", "Indústria", ["https://caoa.gupy.io"]),
    ("BYD Brasil", "Indústria", ["https://byd.gupy.io"]),
    ("GWM Brasil", "Indústria", ["https://gwm.gupy.io"]),
    ("Flex Brasil", "Indústria", ["https://flex.gupy.io"]),
    ("Jabil Brasil", "Indústria", ["https://jabil.gupy.io"]),
    ("Continental Brasil", "Indústria", ["https://continental.gupy.io"]),
    ("ZF do Brasil", "Indústria", ["https://zf.gupy.io"]),
    ("Mahle", "Indústria", ["https://mahle.gupy.io"]),
    ("Eaton", "Indústria", ["https://eaton.gupy.io"]),
    ("Pirelli Brasil", "Indústria", ["https://pirelli.gupy.io"]),
    ("Michelin", "Indústria", ["https://michelin.gupy.io"]),
    ("Bridgestone Brasil", "Indústria", ["https://bridgestone.gupy.io"]),
    ("Goodyear Brasil", "Indústria", ["https://goodyear.gupy.io"]),
    ("Eldorado Brasil", "Indústria", ["https://eldorado.gupy.io"]),
    ("Bracell", "Indústria", ["https://bracell.gupy.io"]),
    ("Irani", "Indústria", ["https://irani.gupy.io"]),
    ("International Paper Brasil", "Indústria", ["https://internationalpaper.gupy.io"]),
    ("Smurfit Kappa", "Indústria", ["https://smurfitkappa.gupy.io"]),
    ("Verallia", "Indústria", ["https://verallia.gupy.io"]),
    ("Cebrace", "Indústria", ["https://cebrace.gupy.io"]),
    ("AGC Brasil", "Indústria", ["https://agc.gupy.io"]),
    ("Unipar", "Indústria", ["https://unipar.gupy.io"]),
    ("Lanxess", "Indústria", ["https://lanxess.gupy.io"]),
    ("Clariant", "Indústria", ["https://clariant.gupy.io"]),
    ("Evonik", "Indústria", ["https://evonik.gupy.io"]),
    ("AkzoNobel", "Indústria", ["https://akzonobel.gupy.io"]),
    ("Sherwin-Williams", "Indústria", ["https://sherwinwilliams.gupy.io"]),
    ("PPG", "Indústria", ["https://ppg.gupy.io"]),
    ("Suvinil", "Indústria", ["https://suvinil.gupy.io"]),
    ("Tintas Coral", "Indústria", ["https://coral.gupy.io"]),
    ("Aperam", "Indústria", ["https://aperam.gupy.io"]),
    ("Ternium Brasil", "Indústria", ["https://ternium.gupy.io"]),
    ("Ferbasa", "Indústria", ["https://ferbasa.gupy.io"]),
    ("Paranapanema", "Indústria", ["https://paranapanema.gupy.io"]),
    ("Mangels", "Indústria", ["https://mangels.gupy.io"]),
    ("InterCement", "Indústria", ["https://intercement.gupy.io"]),
    ("Holcim Brasil", "Indústria", ["https://holcim.gupy.io"]),
    ("Tigre", "Indústria", ["https://tigre.gupy.io"]),
    ("Amanco", "Indústria", ["https://amanco.gupy.io"]),
    ("Deca", "Indústria", ["https://deca.gupy.io"]),
    ("Roca Brasil", "Indústria", ["https://roca.gupy.io"]),
    ("Knauf", "Indústria", ["https://knauf.gupy.io"]),
    ("Eternit", "Indústria", ["https://eternit.gupy.io"]),
    ("Whirlpool Brasil", "Indústria", ["https://whirlpool.gupy.io"]),
    ("Electrolux Brasil", "Indústria", ["https://electrolux.gupy.io"]),
    ("Mondial", "Indústria", ["https://mondial.gupy.io"]),
    ("Britânia", "Indústria", ["https://britania.gupy.io"]),
    ("Cadence", "Indústria", ["https://cadence.gupy.io"]),
    ("Arno", "Indústria", ["https://arno.gupy.io"]),
    ("Mueller Eletrodomésticos", "Indústria", ["https://mueller.gupy.io"]),
    ("Bosch Brasil", "Indústria", ["https://bosch.gupy.io"]),
    ("Siemens Brasil", "Indústria", ["https://siemens.gupy.io"]),
    ("ABB Brasil", "Indústria", ["https://abb.gupy.io"]),
    ("Schneider Electric Brasil", "Indústria", ["https://schneider.gupy.io"]),
    ("Bayer Brasil", "Indústria", ["https://bayer.gupy.io"]),
    ("BASF Brasil", "Indústria", ["https://basf.gupy.io"]),
    ("Dow Brasil", "Indústria", ["https://dow.gupy.io"]),
    ("DuPont Brasil", "Indústria", ["https://dupont.gupy.io"]),
    ("Syngenta Brasil", "Indústria", ["https://syngenta.gupy.io"]),
    ("Corteva Agriscience", "Indústria", ["https://corteva.gupy.io"]),
    ("John Deere", "Indústria", ["https://johndeere.gupy.io"]),
    ("CNH Industrial", "Indústria", ["https://cnhindustrial.gupy.io"]),
    ("Agrale", "Indústria", ["https://agrale.gupy.io"]),
    ("Jacto", "Indústria", ["https://jacto.gupy.io"]),
    ("Kepler Weber", "Indústria", ["https://keplerweber.gupy.io"]),
    # Energia e Utilities
    ("Claro", "Energia e Utilities", ["https://vempraclaro.gupy.io"]),
    ("Vivo", "Energia e Utilities", ["https://vivo.gupy.io"]),
    ("TIM", "Energia e Utilities", ["https://carreiras.gupy.io/tim"]),
    ("V.tal", "Energia e Utilities", ["https://vtal.gupy.io"]),
    ("Energisa", "Energia e Utilities", ["https://energisa.gupy.io"]),
    ("Light", "Energia e Utilities", ["https://light.gupy.io"]),
    ("Enel Brasil", "Energia e Utilities", ["https://enel.gupy.io"]),
    ("Sabesp", "Energia e Utilities", ["https://sabesp.gupy.io"]),
    ("Sanepar", "Energia e Utilities", ["https://sanepar.gupy.io"]),
    ("Copasa", "Energia e Utilities", ["https://copasa.gupy.io"]),
    ("Comgás", "Energia e Utilities", ["https://comgas.gupy.io"]),
    ("3R Petroleum", "Energia e Utilities", ["https://3rpetroleum.gupy.io"]),
    ("PetroRio", "Energia e Utilities", ["https://petrorio.gupy.io"]),
    ("PRIO", "Energia e Utilities", ["https://prio.gupy.io"]),
    ("Taesa", "Energia e Utilities", ["https://taesa.gupy.io"]),
    ("Isa CTEEP", "Energia e Utilities", ["https://cteep.gupy.io"]),
    ("Auren", "Energia e Utilities", ["https://auren.gupy.io"]),
    ("Omega Energia", "Energia e Utilities", ["https://omegaenergia.gupy.io"]),
    ("Casa dos Ventos", "Energia e Utilities", ["https://casadosventos.gupy.io"]),
    ("Renova Energia", "Energia e Utilities", ["https://renovaenergia.gupy.io"]),
    ("Alupar", "Energia e Utilities", ["https://alupar.gupy.io"]),
    ("Statkraft Brasil", "Energia e Utilities", ["https://statkraft.gupy.io"]),
    ("Voltalia", "Energia e Utilities", ["https://voltalia.gupy.io"]),
    ("Acciona", "Energia e Utilities", ["https://acciona.gupy.io"]),
    ("Shell Brasil", "Energia e Utilities", ["https://shell.gupy.io"]),
    ("Total Energies Brasil", "Energia e Utilities", ["https://totalenergies.gupy.io"]),
    ("Equinor", "Energia e Utilities", ["https://equinor.gupy.io"]),
    ("BP Brasil", "Energia e Utilities", ["https://bp.gupy.io"]),
    ("Chevron Brasil", "Energia e Utilities", ["https://chevron.gupy.io"]),
    ("ExxonMobil Brasil", "Energia e Utilities", ["https://exxonmobil.gupy.io"]),
    ("Naturgy", "Energia e Utilities", ["https://naturgy.gupy.io"]),
    ("Galp Brasil", "Energia e Utilities", ["https://galp.gupy.io"]),
    ("Brisanet", "Energia e Utilities", ["https://brisanet.gupy.io"]),
    ("Desktop", "Energia e Utilities", ["https://desktop.gupy.io"]),
    ("Unifique", "Energia e Utilities", ["https://unifique.gupy.io"]),
    ("Vero Internet", "Energia e Utilities", ["https://vero.gupy.io"]),
    ("Sercomtel", "Energia e Utilities", ["https://sercomtel.gupy.io"]),
    ("Embratel", "Energia e Utilities", ["https://embratel.gupy.io"]),
    ("Alloha Fibra", "Energia e Utilities", ["https://allohafibra.gupy.io"]),
    ("Cedae", "Energia e Utilities", ["https://cedae.gupy.io"]),
    ("Caesb", "Energia e Utilities", ["https://caesb.gupy.io"]),
    ("Compesa", "Energia e Utilities", ["https://compesa.gupy.io"]),
    ("Embasa", "Energia e Utilities", ["https://embasa.gupy.io"]),
    ("Casan", "Energia e Utilities", ["https://casan.gupy.io"]),
    ("Cagece", "Energia e Utilities", ["https://cagece.gupy.io"]),
    ("Iguá Saneamento", "Energia e Utilities", ["https://igua.gupy.io"]),
    ("Águas do Brasil", "Energia e Utilities", ["https://aguasdobrasil.gupy.io"]),
    ("GS Inima", "Energia e Utilities", ["https://gsinima.gupy.io"]),
    ("Solvi", "Energia e Utilities", ["https://solvi.gupy.io"]),
    ("Estre Ambiental", "Energia e Utilities", ["https://estreambiental.gupy.io"]),
    ("Orizon", "Energia e Utilities", ["https://orizon.gupy.io"]),
    # Logística e Mobilidade
    ("Simpar", "Logística e Mobilidade", ["https://simpar.gupy.io"]),
    ("Vamos", "Logística e Mobilidade", ["https://vamos.gupy.io"]),
    ("Tegma", "Logística e Mobilidade", ["https://tegma.gupy.io"]),
    ("Jadlog", "Logística e Mobilidade", ["https://jadlog.gupy.io"]),
    ("DHL Brasil", "Logística e Mobilidade", ["https://dhl.gupy.io"]),
    ("FedEx Brasil", "Logística e Mobilidade", ["https://fedex.gupy.io"]),
    ("UPS Brasil", "Logística e Mobilidade", ["https://ups.gupy.io"]),
    ("Kuehne Nagel", "Logística e Mobilidade", ["https://kuehne-nagel.gupy.io"]),
    ("DB Schenker", "Logística e Mobilidade", ["https://dbschenker.gupy.io"]),
    ("Geodis", "Logística e Mobilidade", ["https://geodis.gupy.io"]),
    ("Mainfreight", "Logística e Mobilidade", ["https://mainfreight.gupy.io"]),
    ("CEVA Logistics", "Logística e Mobilidade", ["https://cevalogistics.gupy.io"]),
    ("XPO Logistics", "Logística e Mobilidade", ["https://xpo.gupy.io"]),
    ("GLP Brasil", "Logística e Mobilidade", ["https://glp.gupy.io"]),
    ("Prologis", "Logística e Mobilidade", ["https://prologis.gupy.io"]),
    ("ID Logistics", "Logística e Mobilidade", ["https://idlogistics.gupy.io"]),
    ("Penske Logistics", "Logística e Mobilidade", ["https://penske.gupy.io"]),
    ("Buser", "Logística e Mobilidade", ["https://buser.gupy.io"]),
    ("FlixBus", "Logística e Mobilidade", ["https://flixbus.gupy.io"]),
    ("AENA Brasil", "Logística e Mobilidade", ["https://aena.gupy.io"]),
    ("GRU Airport", "Logística e Mobilidade", ["https://gruairport.gupy.io"]),
    ("Infraero", "Logística e Mobilidade", ["https://infraero.gupy.io"]),
    ("ANAC", "Logística e Mobilidade", ["https://anac.gupy.io"]),
    ("Hidrovias do Brasil", "Logística e Mobilidade", ["https://hidrovias.gupy.io"]),
    ("Santos Brasil", "Logística e Mobilidade", ["https://santosbrasil.gupy.io"]),
    ("MRS Logística", "Logística e Mobilidade", ["https://mrslogistica.gupy.io"]),
    ("VLI", "Logística e Mobilidade", ["https://vli-logistica.gupy.io"]),
    ("Wilson Sons", "Logística e Mobilidade", ["https://wilsonsons.gupy.io"]),
    # Construção e Imóveis
    ("Direcional", "Construção e Imóveis", ["https://direcional.gupy.io"]),
    ("Trisul", "Construção e Imóveis", ["https://trisul.gupy.io"]),
    ("Lavvi", "Construção e Imóveis", ["https://lavvi.gupy.io"]),
    ("Eztec", "Construção e Imóveis", ["https://eztec.gupy.io"]),
    ("Gafisa", "Construção e Imóveis", ["https://gafisa.gupy.io"]),
    ("PDG Realty", "Construção e Imóveis", ["https://pdg.gupy.io"]),
    ("Rossi Residencial", "Construção e Imóveis", ["https://rossi.gupy.io"]),
    ("Moura Dubeux", "Construção e Imóveis", ["https://mouradubeux.gupy.io"]),
    ("RNI", "Construção e Imóveis", ["https://rni.gupy.io"]),
    ("Cury", "Construção e Imóveis", ["https://cury.gupy.io"]),
    ("Living", "Construção e Imóveis", ["https://living.gupy.io"]),
    ("OAS", "Construção e Imóveis", ["https://oas.gupy.io"]),
    ("Novonor", "Construção e Imóveis", ["https://novonor.gupy.io"]),
    ("Construcap", "Construção e Imóveis", ["https://construcap.gupy.io"]),
    ("Mendes Júnior", "Construção e Imóveis", ["https://mendesjunior.gupy.io"]),
    ("Galvão Engenharia", "Construção e Imóveis", ["https://galvaoengenharia.gupy.io"]),
    ("Queiroz Galvão", "Construção e Imóveis", ["https://queirozgalvao.gupy.io"]),
    ("Brookfield Brasil", "Construção e Imóveis", ["https://brookfield.gupy.io"]),
    ("Cushman & Wakefield", "Construção e Imóveis", ["https://cushmanwakefield.gupy.io"]),
    ("CBRE", "Construção e Imóveis", ["https://cbre.gupy.io"]),
    ("JLL", "Construção e Imóveis", ["https://jll.gupy.io"]),
    ("Colliers", "Construção e Imóveis", ["https://colliers.gupy.io"]),
    ("Newmark", "Construção e Imóveis", ["https://newmark.gupy.io"]),
    ("Lopes Imóveis", "Construção e Imóveis", ["https://lopes.gupy.io"]),
    ("RE/MAX", "Construção e Imóveis", ["https://remax.gupy.io"]),
    ("Auxiliadora Predial", "Construção e Imóveis", ["https://auxiliadorapredial.gupy.io"]),
    ("Coelho da Fonseca", "Construção e Imóveis", ["https://coelhodafonseca.gupy.io"]),
    ("Aliansce Sonae", "Construção e Imóveis", ["https://alianscesonae.gupy.io"]),
    ("LOG Commercial Properties", "Construção e Imóveis", ["https://logcp.gupy.io"]),
    ("BR Properties", "Construção e Imóveis", ["https://brproperties.gupy.io"]),
    ("Iguatemi", "Construção e Imóveis", ["https://iguatemi.gupy.io"]),
    ("Multiplan", "Construção e Imóveis", ["https://multiplan.gupy.io"]),
    ("BrMalls", "Construção e Imóveis", ["https://brmalls.gupy.io"]),
    # Educação
    ("FGV", "Educação", ["https://portal.fgv.br/trabalhe-conosco"]),
    ("Insper", "Educação", ["https://insper.gupy.io"]),
    ("ESPM", "Educação", ["https://espm.gupy.io"]),
    ("Rocketseat", "Educação", ["https://rocketseat.gupy.io"]),
    ("Wizard", "Educação", ["https://wizard.gupy.io"]),
    ("Wise Up", "Educação", ["https://wiseup.gupy.io"]),
    ("CCAA", "Educação", ["https://ccaa.gupy.io"]),
    ("Fisk", "Educação", ["https://fisk.gupy.io"]),
    ("Bernoulli", "Educação", ["https://bernoulli.gupy.io"]),
    ("Poliedro", "Educação", ["https://poliedro.gupy.io"]),
    ("Unicesumar", "Educação", ["https://unicesumar.gupy.io"]),
    ("Anhanguera", "Educação", ["https://anhanguera.gupy.io"]),
    ("Unopar", "Educação", ["https://unopar.gupy.io"]),
    ("Pearson", "Educação", ["https://pearson.gupy.io"]),
    ("Elsevier", "Educação", ["https://elsevier.gupy.io"]),
    ("Maple Bear", "Educação", ["https://maplebear.gupy.io"]),
    ("Anglo", "Educação", ["https://anglo.gupy.io"]),
    ("Etapa", "Educação", ["https://etapa.gupy.io"]),
    ("Objetivo", "Educação", ["https://objetivo.gupy.io"]),
    ("Conquer", "Educação", ["https://conquer.gupy.io"]),
    ("Geekie", "Educação", ["https://geekie.gupy.io"]),
    ("Stoodi", "Educação", ["https://stoodi.gupy.io"]),
    ("DIO", "Educação", ["https://dio.gupy.io"]),
    ("Cubos Academy", "Educação", ["https://cubos.gupy.io"]),
    ("PM3", "Educação", ["https://pm3.gupy.io"]),
    ("Mentorama", "Educação", ["https://mentorama.gupy.io"]),
    ("Tera", "Educação", ["https://tera.gupy.io"]),
    ("Reprograma", "Educação", ["https://reprograma.gupy.io"]),
    ("PrograMaria", "Educação", ["https://programaria.gupy.io"]),
    ("Kenzie Academy", "Educação", ["https://kenzie.gupy.io"]),
    ("Open English", "Educação", ["https://openenglish.gupy.io"]),
    ("Coursera", "Educação", ["https://careers.coursera.com"]),
    ("Udemy", "Educação", ["https://about.udemy.com/careers"]),
    ("Duolingo", "Educação", ["https://careers.duolingo.com"]),
    # Agro e Alimentos
    ("Jalles Machado", "Agro e Alimentos", ["https://jallesmachado.gupy.io"]),
    ("Atvos", "Agro e Alimentos", ["https://atvos.gupy.io"]),
    ("Caramuru Alimentos", "Agro e Alimentos", ["https://caramuru.gupy.io"]),
    ("Granol", "Agro e Alimentos", ["https://granol.gupy.io"]),
    ("Vittia", "Agro e Alimentos", ["https://vittia.gupy.io"]),
    ("Boa Safra Sementes", "Agro e Alimentos", ["https://boasafra.gupy.io"]),
    ("Mosaic", "Agro e Alimentos", ["https://mosaic.gupy.io"]),
    ("Ouro Fino Saúde Animal", "Agro e Alimentos", ["https://ourofino.gupy.io"]),
    ("Biotrop", "Agro e Alimentos", ["https://biotrop.gupy.io"]),
    ("ICL Brasil", "Agro e Alimentos", ["https://icl.gupy.io"]),
    ("Galvani", "Agro e Alimentos", ["https://galvani.gupy.io"]),
    ("OCP Brasil", "Agro e Alimentos", ["https://ocp.gupy.io"]),
    ("Ferrero Brasil", "Agro e Alimentos", ["https://ferrero.gupy.io"]),
    ("Mars Brasil", "Agro e Alimentos", ["https://mars.gupy.io"]),
    ("Kraft Heinz", "Agro e Alimentos", ["https://kraftheinz.gupy.io"]),
    ("Kellogg's", "Agro e Alimentos", ["https://kelloggs.gupy.io"]),
    ("Tnuva", "Agro e Alimentos", ["https://tnuva.gupy.io"]),
    ("Pif Paf", "Agro e Alimentos", ["https://pifpaf.gupy.io"]),
    ("Plena Alimentos", "Agro e Alimentos", ["https://plena.gupy.io"]),
    ("Pamplona Alimentos", "Agro e Alimentos", ["https://pamplona.gupy.io"]),
    ("Frigol", "Agro e Alimentos", ["https://frigol.gupy.io"]),
    ("Tyson Foods Brasil", "Agro e Alimentos", ["https://tyson.gupy.io"]),
    ("Coamo", "Agro e Alimentos", ["https://coamo.gupy.io"]),
    ("Coopavel", "Agro e Alimentos", ["https://coopavel.gupy.io"]),
    ("C.Vale", "Agro e Alimentos", ["https://cvale.gupy.io"]),
    ("Coopercitrus", "Agro e Alimentos", ["https://coopercitrus.gupy.io"]),
    ("Castrolanda", "Agro e Alimentos", ["https://castrolanda.gupy.io"]),
    ("Cocamar", "Agro e Alimentos", ["https://cocamar.gupy.io"]),
    ("Cotrijal", "Agro e Alimentos", ["https://cotrijal.gupy.io"]),
    ("Lar Cooperativa Agroindustrial", "Agro e Alimentos", ["https://lar.gupy.io"]),
    ("Adecoagro", "Agro e Alimentos", ["https://adecoagro.gupy.io"]),
    ("Terra Santa", "Agro e Alimentos", ["https://terrasanta.gupy.io"]),
    ("Stara", "Agro e Alimentos", ["https://stara.gupy.io"]),
    ("Valtra", "Agro e Alimentos", ["https://valtra.gupy.io"]),
    ("Massey Ferguson", "Agro e Alimentos", ["https://masseyferguson.gupy.io"]),
    ("AGCO", "Agro e Alimentos", ["https://agco.gupy.io"]),
    ("Louis Dreyfus Company", "Agro e Alimentos", ["https://ldc.gupy.io"]),
    ("COFCO International Brasil", "Agro e Alimentos", ["https://cofco.gupy.io"]),
    ("Biosev", "Agro e Alimentos", ["https://biosev.gupy.io"]),
    ("Cocal Energia", "Agro e Alimentos", ["https://cocal.gupy.io"]),
    ("Coruripe", "Agro e Alimentos", ["https://coruripe.gupy.io"]),
    ("Usina Santa Terezinha", "Agro e Alimentos", ["https://santaterezinha.gupy.io"]),
    ("Cristal Pigmentos", "Agro e Alimentos", ["https://cristal.gupy.io"]),
    ("Sealed Air", "Agro e Alimentos", ["https://sealedair.gupy.io"]),
    ("Tetra Pak", "Agro e Alimentos", ["https://tetrapak.gupy.io"]),
    ("Catalent", "Agro e Alimentos", ["https://catalent.gupy.io"]),
    ("Bacardi Brasil", "Agro e Alimentos", ["https://bacardi.gupy.io"]),
    ("Beam Suntory", "Agro e Alimentos", ["https://beamsuntory.gupy.io"]),
    ("Edrington", "Agro e Alimentos", ["https://edrington.gupy.io"]),
    ("Seara", "Agro e Alimentos", ["https://seara.gupy.io"]),
    ("Friboi", "Agro e Alimentos", ["https://friboi.gupy.io"]),
    ("Cutrale", "Agro e Alimentos", ["https://cutrale.gupy.io"]),
    ("Copersucar", "Agro e Alimentos", ["https://copersucar.gupy.io"]),
    ("Savegnago", "Agro e Alimentos", ["https://savegnago.gupy.io"]),
    ("Comper", "Agro e Alimentos", ["https://comper.gupy.io"]),
    ("Bistek", "Agro e Alimentos", ["https://bistek.gupy.io"]),
    ("Zaffari", "Agro e Alimentos", ["https://zaffari.gupy.io"]),
    ("Muffato", "Agro e Alimentos", ["https://muffato.gupy.io"]),
    ("Cooperativa Santa Clara", "Agro e Alimentos", ["https://santaclara.gupy.io"]),
    ("Cooperativa Três Tentos", "Agro e Alimentos", ["https://3tentos.gupy.io"]),
    # Mídia e Entretenimento
    ("SBT", "Mídia e Entretenimento", ["https://sbt.gupy.io"]),
    ("CNN Brasil", "Mídia e Entretenimento", ["https://cnnbrasil.gupy.io"]),
    ("Jovem Pan", "Mídia e Entretenimento", ["https://jovempan.gupy.io"]),
    ("Estadão", "Mídia e Entretenimento", ["https://estadao.gupy.io"]),
    ("Grupo Estado", "Mídia e Entretenimento", ["https://estadao.gupy.io"]),
    ("O Estado de S. Paulo", "Mídia e Entretenimento", ["https://estadao.gupy.io"]),
    ("Grupo Folha", "Mídia e Entretenimento", ["https://folha.gupy.io"]),
    ("Folha de S.Paulo", "Mídia e Entretenimento", ["https://folha.gupy.io"]),
    ("Valor Econômico", "Mídia e Entretenimento", ["https://valor.gupy.io"]),
    ("InfoMoney", "Mídia e Entretenimento", ["https://infomoney.gupy.io"]),
    ("Exame", "Mídia e Entretenimento", ["https://exame.gupy.io"]),
    ("Veja", "Mídia e Entretenimento", ["https://veja.gupy.io"]),
    ("Grupo Abril", "Mídia e Entretenimento", ["https://abril.gupy.io"]),
    ("Editora Saraiva", "Mídia e Entretenimento", ["https://saraiva.gupy.io"]),
    ("FTD Educação", "Mídia e Entretenimento", ["https://ftd.gupy.io"]),
    ("Moderna", "Mídia e Entretenimento", ["https://moderna.gupy.io"]),
    ("Ática", "Mídia e Entretenimento", ["https://atica.gupy.io"]),
    ("Scipione", "Mídia e Entretenimento", ["https://scipione.gupy.io"]),
    ("Cinemark", "Mídia e Entretenimento", ["https://cinemark.gupy.io"]),
    ("Cinépolis", "Mídia e Entretenimento", ["https://cinepolis.gupy.io"]),
    ("Time For Fun", "Mídia e Entretenimento", ["https://t4f.gupy.io"]),
    ("T4F", "Mídia e Entretenimento", ["https://t4f.gupy.io"]),
    ("Netflix Brasil", "Mídia e Entretenimento", ["https://jobs.netflix.com"]),
    ("Disney Brasil", "Mídia e Entretenimento", ["https://jobs.disneycareers.com"]),
    ("Electronic Arts", "Mídia e Entretenimento", ["https://ea.gr8people.com"]),
    ("Riot Games Brasil", "Mídia e Entretenimento", ["https://riotgames.com/careers"]),
    ("Grupo Globo", "Mídia e Entretenimento", ["https://globo.gupy.io"]),
    ("Record TV", "Mídia e Entretenimento", ["https://recordtv.gupy.io"]),
    ("RedeTV", "Mídia e Entretenimento", ["https://redetv.gupy.io"]),
    ("BandNews", "Mídia e Entretenimento", ["https://bandnews.gupy.io"]),
    ("São Paulo Turismo", "Mídia e Entretenimento", ["https://saopauloturismo.gupy.io"]),
    # Serviços e Outros
    ("Manserv", "Serviços e Outros", ["https://manserv.gupy.io"]),
    ("GPS Group", "Serviços e Outros", ["https://gps.gupy.io"]),
    ("Tahto", "Serviços e Outros", ["https://tahto.gupy.io"]),
    ("Liq Corp", "Serviços e Outros", ["https://liq.gupy.io"]),
    ("Verzani & Sandrini", "Serviços e Outros", ["https://verzani.gupy.io"]),
    ("Concentrix", "Serviços e Outros", ["https://concentrix.gupy.io"]),
    ("Webhelp", "Serviços e Outros", ["https://webhelp.gupy.io"]),
    ("Foundever", "Serviços e Outros", ["https://foundever.gupy.io"]),
    ("Sitel", "Serviços e Outros", ["https://sitel.gupy.io"]),
    ("AeC", "Serviços e Outros", ["https://aec.gupy.io"]),
    ("CSU Cardsystem", "Serviços e Outros", ["https://csu.gupy.io"]),
    ("Almaviva do Brasil", "Serviços e Outros", ["https://almaviva.gupy.io"]),
    ("GR Serviços", "Serviços e Outros", ["https://grservicos.gupy.io"]),
    ("Protiviti", "Serviços e Outros", ["https://protiviti.gupy.io"]),
    ("Falconi", "Serviços e Outros", ["https://falconi.gupy.io"]),
    ("Integration Consulting", "Serviços e Outros", ["https://integration.gupy.io"]),
    ("RSM Brasil", "Serviços e Outros", ["https://rsm.gupy.io"]),
    ("BDO", "Serviços e Outros", ["https://bdo.gupy.io"]),
    ("Grant Thornton", "Serviços e Outros", ["https://grantthornton.gupy.io"]),
    ("Mazars", "Serviços e Outros", ["https://mazars.gupy.io"]),
    ("Crowe", "Serviços e Outros", ["https://crowe.gupy.io"]),
    ("Hays Brasil", "Serviços e Outros", ["https://hays.gupy.io"]),
    ("Michael Page", "Serviços e Outros", ["https://michaelpage.gupy.io"]),
    ("PageGroup", "Serviços e Outros", ["https://pagegroup.gupy.io"]),
    ("Korn Ferry", "Serviços e Outros", ["https://kornferry.gupy.io"]),
    ("Spencer Stuart", "Serviços e Outros", ["https://spencerstuart.gupy.io"]),
    ("Heidrick & Struggles", "Serviços e Outros", ["https://heidrick.gupy.io"]),
    ("Egon Zehnder", "Serviços e Outros", ["https://egonzehnder.gupy.io"]),
    ("Russell Reynolds", "Serviços e Outros", ["https://russellreynolds.gupy.io"]),
    ("Roland Berger", "Serviços e Outros", ["https://rolandberger.gupy.io"]),
    ("Oliver Wyman", "Serviços e Outros", ["https://oliverwyman.gupy.io"]),
    ("Kearney", "Serviços e Outros", ["https://kearney.gupy.io"]),
    ("AT Kearney", "Serviços e Outros", ["https://kearney.gupy.io"]),
    ("Booz Allen", "Serviços e Outros", ["https://boozallen.gupy.io"]),
    ("Metrô São Paulo", "Serviços e Outros", ["https://metrosp.gupy.io"]),
    ("CPTM", "Serviços e Outros", ["https://cptm.gupy.io"]),
    ("Zamp", "Serviços e Outros", ["https://zamp.gupy.io"]),
    ("Bob's", "Serviços e Outros", ["https://bobs.gupy.io"]),
    ("Habib's", "Serviços e Outros", ["https://habibs.gupy.io"]),
    ("Giraffas", "Serviços e Outros", ["https://giraffas.gupy.io"]),
    ("Subway", "Serviços e Outros", ["https://subway.gupy.io"]),
    ("Domino's Pizza", "Serviços e Outros", ["https://dominos.gupy.io"]),
    ("Pizza Hut", "Serviços e Outros", ["https://pizzahut.gupy.io"]),
    ("KFC", "Serviços e Outros", ["https://kfc.gupy.io"]),
    ("Outback Steakhouse", "Serviços e Outros", ["https://outback.gupy.io"]),
    ("Madero", "Serviços e Outros", ["https://madero.gupy.io"]),
    ("Spoleto", "Serviços e Outros", ["https://spoleto.gupy.io"]),
    ("Vivenda do Camarão", "Serviços e Outros", ["https://vivenda.gupy.io"]),
    ("China in Box", "Serviços e Outros", ["https://chinainbox.gupy.io"]),
    ("Kopenhagen", "Serviços e Outros", ["https://kopenhagen.gupy.io"]),
    ("Chocolates Garoto", "Serviços e Outros", ["https://garoto.gupy.io"]),
    ("The Coffee", "Serviços e Outros", ["https://thecoffee.gupy.io"]),
    ("Casa do Pão de Queijo", "Serviços e Outros", ["https://casadopaodequeijo.gupy.io"]),
    ("Dunkin Donuts", "Serviços e Outros", ["https://dunkin.gupy.io"]),
    ("TotalPass", "Serviços e Outros", ["https://totalpass.gupy.io"]),
    ("Swile", "Serviços e Outros", ["https://jobs.lever.co/swile"]),
    ("Caju", "Serviços e Outros", ["https://caju.gupy.io"]),
    ("Flash", "Serviços e Outros", ["https://flash.inhire.app/vagas"]),
    ("Camargo Corrêa", "Serviços e Outros", ["https://camargocorrea.gupy.io"]),
    ("Andrade Gutierrez", "Serviços e Outros", ["https://andradegutierrez.gupy.io"]),
    ("Ambipar", "Serviços e Outros", ["https://carreiras.gupy.io/ambipar"]),
    ("Foxx", "Serviços e Outros", ["https://foxx.gupy.io"]),
    ("Wiz", "Serviços e Outros", ["https://wiz.gupy.io"]),
]


def norm(name: str) -> str:
    n = unidecode((name or "").lower())
    n = re.sub(r"\s*(s/?a\.?|ltda\.?|holding)\s*", " ", n)
    n = re.sub(r"[^a-z0-9]+", "", n)
    return n.strip()


def load_existing() -> set[str]:
    import yaml

    names = set()
    with open(YAML_PATH, encoding="utf-8") as f:
        for c in yaml.safe_load(f).get("companies", []):
            names.add(norm(c["name"]))
    with open(LIST_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            names.add(norm(row["Nome da Empresa"]))
    return names


def load_discovered() -> list[tuple[str, str, list[str]]]:
    out = []
    for path in [
        ROOT / "artifacts/discovered_urls_clean.json",
        ROOT / "artifacts/discovered_urls_pass2.json",
    ]:
        if not path.exists():
            continue
        for item in json.loads(path.read_text(encoding="utf-8")):
            out.append((item["name"], item["macro"], item["urls"]))
    return out


def verify_entry(name: str, macro: str, urls: list[str], session) -> dict | None:
    good = []
    for u in urls:
        u = clean_url(u)
        if verify_website_status(session, u)["status"] != "1":
            continue
        if not verify_portal_has_jobs(u, session):
            continue
        if u not in good:
            good.append(u)
        if len(good) >= 3:
            break
    if not good:
        return None
    return {"name": name, "macro": macro, "urls": good}


def render_yaml(entries: list[dict]) -> str:
    by_macro: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_macro[e["macro"]].append(e)

    order = [
        "Financeiro", "Tecnologia", "Varejo e Consumo", "Saúde", "Indústria",
        "Energia e Utilities", "Logística e Mobilidade", "Construção e Imóveis",
        "Educação", "Agro e Alimentos", "Mídia e Entretenimento", "Serviços e Outros",
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
    existing = load_existing()
    candidates: list[tuple[str, str, list[str]]] = []
    seen = set()

    def add(name: str, macro: str, urls: list[str]):
        k = norm(name)
        if not k or k in seen or k in existing:
            return
        seen.add(k)
        candidates.append((name, macro, urls))

    for name, macro, urls in BATCH + load_discovered():
        add(name, macro, urls)

    print(f"Candidates to verify: {len(candidates)}")
    session = create_shared_session()
    verified: list[dict] = []

    def work(c):
        return verify_entry(c[0], c[1], c[2], session)

    with ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(work, c): c for c in candidates}
        done = 0
        for fut in as_completed(futs):
            done += 1
            res = fut.result()
            if res:
                verified.append(res)
                print(f"+ [{len(verified)}] {res['name']} -> {res['urls'][0]}")
            if done % 50 == 0:
                print(f"  {done}/{len(candidates)}")

    verified.sort(key=lambda x: (x["macro"], x["name"].lower()))
    print(f"\nVerified: {len(verified)}")
    OUT_PATH.write_text(render_yaml(verified), encoding="utf-8")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
