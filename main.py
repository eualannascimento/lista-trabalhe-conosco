import csv
import logging
import sys
from datetime import date

from unidecode import unidecode

from src.py.functions.df_operations import clean_url
from src.py.functions.file_operations import read_and_filter_csv, read_csv, save_sorted_csv
from src.py.functions.md_operations import generate_markdown_table, load_header
from src.py.functions.website_verification import verify_websites_concurrent

# Caminhos dos arquivos
NEW_ITEMS_FILE = "src/data/input/new_items.csv"
LIST_FILE_PATH = "src/data/input/list.csv"
HEADER_FILE_PATH = "src/data/input/header.md"
README_FILE_PATH = "README.md"

FIELDNAMES = [
    "Status da URL",
    "Data de Entrada",
    "Nome da Empresa",
    "Segmento da Empresa",
    "Plataforma",
    "URL",
    "Data de Publicação",
]

logger = logging.getLogger(__name__)


def setup_logging():
    """Configura o logging com formato padronizado para console."""
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)


def process_new_items(new_items_file, list_file_path):
    """
    Lê novos itens de new_items.csv, deduplica contra list.csv,
    e adiciona os novos à lista existente.
    Retorna (quantidade_adicionados, lista_duplicados).
    """
    with open(new_items_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        new_items = list(reader)

    if not new_items:
        logger.info("Nenhum novo item encontrado em %s", new_items_file)
        return 0, []

    logger.info("Encontrados %d novos itens em %s", len(new_items), new_items_file)
    for item in new_items:
        logger.info("  -> %s | %s", item.get("Nome da Empresa", "?"), item.get("URL", "?"))

    existing_items = read_csv(list_file_path)
    existing_urls = set(clean_url(item["URL"]) for item in existing_items)

    added_count = 0
    duplicates = []

    for item in new_items:
        url = item.get("URL")
        name = item.get("Nome da Empresa")
        
        if not url or not name:
            logger.warning("Pulando item inválido: %s", item)
            continue
            
        cleaned_url = clean_url(url)
        if cleaned_url in existing_urls:
            duplicates.append(item)
            logger.warning("Duplicado ignorado: %s | %s", name, cleaned_url)
            continue

        new_row = {
            "Status da URL": "0",
            "Data de Entrada": date.today().strftime("%Y-%m-%d"),
            "Nome da Empresa": item["Nome da Empresa"],
            "Segmento da Empresa": item["Segmento da Empresa"],
            "Plataforma": item["Plataforma"],
            "URL": cleaned_url,
        }
        existing_items.append(new_row)
        existing_urls.add(cleaned_url)
        added_count += 1
        logger.info("Adicionado: %s | %s", item["Nome da Empresa"], cleaned_url)

    if added_count > 0:
        save_sorted_csv(list_file_path, existing_items, FIELDNAMES)
        logger.info("Salvos %d novos itens em %s", added_count, list_file_path)

    # Limpa new_items.csv mantendo cabeçalho
    with open(new_items_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]
        )
        writer.writeheader()

    return added_count, duplicates


def verify_urls(values):
    """
    Verifica o status de todas as URLs concorrentemente.
    Retorna a lista de itens que falharam na verificação.
    """
    today = date.today().strftime("%Y-%m-%d")
    failed_items = verify_websites_concurrent(values)

    for item in values:
        item["Data do Status"] = today

    return failed_items


def sort_and_deduplicate(values):
    """
    Ordena itens primeiro por 'Data de Publicação' (descendente), 
    depois alfabeticamente por nome da empresa, e remove duplicatas de URL.
    Retorna (itens_unicos, itens_duplicados).
    """
    def sort_key(x):
        date_str = x.get("Data de Publicação", "")
        # Empty dates go to the bottom. For descending order, we invert the date comparison by using an empty string for missing
        date_sort = date_str if date_str else "0000-00-00"
        name_sort = unidecode(x["Nome da Empresa"].lower())
        return (-float(date_sort.replace('-', '')), name_sort)

    sorted_values = sorted(values, key=sort_key)

    unique = []
    seen_urls = set()
    duplicates = []

    for item in sorted_values:
        if item["URL"] not in seen_urls:
            seen_urls.add(item["URL"])
            unique.append(item)
        else:
            duplicates.append(item)

    if duplicates:
        logger.warning("Removidas %d entradas duplicadas:", len(duplicates))
        for dup in duplicates:
            logger.warning("  -> %s | %s", dup["Nome da Empresa"], dup["URL"])
    else:
        logger.info("Nenhuma entrada duplicada encontrada.")

    return unique, duplicates


def save_results(values, list_file_path, header_file_path, readme_file_path):
    """
    Remove campo temporário (em cópia), salva CSV e gera README.md.
    """
    # Create clean copies for saving to avoid modifying the objects used in failure report
    to_save = []
    for item in values:
        clean_item = item.copy()
        clean_item.pop("Data do Status", None)
        clean_item.pop("_error", None)
        to_save.append(clean_item)

    save_sorted_csv(list_file_path, to_save, fieldnames=FIELDNAMES)
    logger.info("CSV salvo: %s (%d registros)", list_file_path, len(to_save))

    markdown_table = generate_markdown_table(to_save)
    header_content = load_header(header_file_path)

    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write(f"{header_content}\n\n{markdown_table}")
    logger.info("README.md atualizado: %s", readme_file_path)


def print_failure_report(failed_items):
    """
    Imprime um relatório final detalhado de todos os sites que falharam na verificação.
    Formato solicitado: Uma linha por erro.
    """
    if not failed_items:
        logger.info("-" * 80)
        logger.info("RELATÓRIO FINAL: SUCESSO! Todas as empresas e sites foram confirmados.")
        logger.info("-" * 80)
        return

    # Usando print para garantir que saia no stdout limpo no final, ou logger.error
    # O usuário pediu "no log", então vamos usar logger.
    
    logger.info("")
    logger.info("=" * 80)
    logger.info(f"RELATÓRIO DE FALHAS - {len(failed_items)} SITE(S) NÃO CONFIRMADOS")
    logger.info("Abaixo a lista de empresas e sites que não foi possível confirmar a existência/funcionamento:")
    logger.info("=" * 80)
    
    # Ordenar por nome para facilitar leitura
    sorted_failures = sorted(failed_items, key=lambda x: unidecode(x["Nome da Empresa"].lower()))

    for item in sorted_failures:
        empresa = item.get("Nome da Empresa", "Desconhecida")
        url = item.get("URL", "Sem URL")
        error = item.get("_error", "Erro não especificado")
        
        # Formato de linha única claro
        logger.error(f"[X] {empresa} | URL: {url} | ERRO: {error}")

    logger.info("=" * 80)
    logger.info("Fim do Relatório de Falhas")
    logger.info("=" * 80)


def main():
    setup_logging()

    logger.info("=" * 60)
    logger.info("INÍCIO DA EXECUÇÃO - VALIDAÇÃO DE VAGAS")
    logger.info("=" * 60)

    # 1. Processar novos itens
    logger.info("--- Etapa 1: Processando novos itens ---")
    added, duplicates = process_new_items(NEW_ITEMS_FILE, LIST_FILE_PATH)
    logger.info("Novos itens adicionados: %d | Duplicados ignorados: %d", added, len(duplicates))

    # 2. Ler lista completa
    logger.info("--- Etapa 2: Lendo lista completa ---")
    values = read_and_filter_csv(LIST_FILE_PATH)
    logger.info("Total de itens na lista: %d", len(values))

    # 3. Verificar URLs
    logger.info("--- Etapa 3: Verificando URLs (Validando existência e status) ---")
    failed_items = verify_urls(values)

    # 4. Ordenar e deduplicar
    logger.info("--- Etapa 4: Ordenando e removendo duplicatas ---")
    unique_values, _ = sort_and_deduplicate(values)

    # 5. Salvar resultados
    logger.info("--- Etapa 5: Salvando resultados ---")
    save_results(unique_values, LIST_FILE_PATH, HEADER_FILE_PATH, README_FILE_PATH)

    # 6. Relatório final de falhas (Executado por último para destaque)
    print_failure_report(failed_items)

    logger.info("=" * 60)
    logger.info("EXECUÇÃO FINALIZADA")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
