import csv
import logging

from .df_operations import clean_url

logger = logging.getLogger(__name__)


def read_and_filter_csv(file_path):
    """Lê o arquivo CSV e retorna uma lista com os dados, limpando as URLs."""
    data = read_csv(file_path)
    for row in data:
        row["URL"] = clean_url(row["URL"])
    logger.info("Lidos %d registros de %s (com URLs limpas)", len(data), file_path)
    return data


def read_csv(file_path):
    """Lê o arquivo CSV completo e retorna uma lista de dicionários."""
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    logger.debug("Lidos %d registros de %s", len(data), file_path)
    return data


def save_sorted_csv(file_path, data, fieldnames):
    """Salva os dados no arquivo CSV com os campos especificados."""
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
    logger.debug("Salvos %d registros em %s", len(data), file_path)
