# file_operations.py
import csv
from .df_operations import clean_url

def read_and_filter_csv(file_path):
    """Lê o arquivo CSV e retorna uma lista com os dados, limpando as URLs."""
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [
            {**row, 'URL': clean_url(row['URL'])}
            for row in reader
        ]
    return data

def read_csv(file_path):
    """Lê o arquivo CSV completo (sem filtragem) e retorna uma lista de dicionários."""
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_sorted_csv(file_path, data, fieldnames):
    """Salva os dados ordenados no arquivo CSV."""
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
