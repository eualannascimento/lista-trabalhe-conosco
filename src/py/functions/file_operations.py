# file_operations.py

import csv
from .df_operations import clean_url

def read_and_filter_csv(file_path):
    """Lê o arquivo CSV, filtra valores ativos e retorna uma lista."""
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        filtered_values = [
            {**row, 'URL': clean_url(row['URL'])}  # Limpa a URL diretamente
            for row in reader if row.get('Status da URL') == '1'
        ]
    return filtered_values

def save_sorted_csv(file_path, data, fieldnames):
    """Salva os dados ordenados no arquivo CSV."""
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)