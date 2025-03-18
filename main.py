# %% 
import csv
from datetime import date
from src.py.functions.file_operations import read_csv, save_sorted_csv, read_and_filter_csv
from src.py.functions.df_operations import clean_url
from src.py.functions.md_operations import generate_markdown_table, load_header
from src.py.functions.website_verification import verify_website_status
from unidecode import unidecode

# Caminhos dos arquivos
NEW_ITEMS_FILE = 'src/data/input/new_items.csv'
LIST_FILE_PATH = 'src/data/input/list.csv'
HEADER_FILE_PATH = 'src/data/input/header.md'
README_FILE_PATH = 'README.md'

# %% 
# PROCESSA NOVOS ITENS (new_items.csv)
with open(NEW_ITEMS_FILE, 'r', newline='', encoding='utf-8') as new_file:
    reader = csv.DictReader(new_file)
    new_items = list(reader)

if new_items:
    # Lê todos os itens já presentes no list.csv
    existing_items = read_csv(LIST_FILE_PATH)
    # Cria um conjunto com as URLs já existentes (após limpeza)
    existing_urls = set(clean_url(item['URL']) for item in existing_items)
    new_entries_added = False

    for item in new_items:
        cleaned_url = clean_url(item['URL'])
        if cleaned_url in existing_urls:
            continue
        # Prepara nova linha com os campos extras
        new_row = {
            'Nome da Empresa': item['Nome da Empresa'],
            'Segmento da Empresa': item['Segmento da Empresa'],
            'Plataforma': item['Plataforma'],
            'URL': cleaned_url,
            'Status da URL': '0',
            'Data de Entrada': date.today().strftime("%Y-%m-%d")
        }
        existing_items.append(new_row)
        existing_urls.add(cleaned_url)
        new_entries_added = True

    if new_entries_added:
        # Define a ordem dos campos para list.csv
        fieldnames = ['Nome da Empresa', 'Segmento da Empresa', 'Plataforma', 'URL', 'Status da URL', 'Data de Entrada']
        save_sorted_csv(LIST_FILE_PATH, existing_items, fieldnames)
    
    # Limpa o arquivo new_items.csv, mantendo apenas o cabeçalho
    with open(NEW_ITEMS_FILE, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=['Nome da Empresa', 'Segmento da Empresa', 'Plataforma', 'URL'])
        writer.writeheader()

# %% 
# FLUXO PRINCIPAL
# 1. Ler e processar dados de list.csv
values = read_and_filter_csv(LIST_FILE_PATH)

# 2. Verificar status das URLs (atualiza para '1' se acessível ou mantém '0')
for value in values:
    url = value['URL']
    value['Status da URL'] = verify_website_status(url)
    value['Data do Status'] = date.today().strftime("%Y-%m-%d")

# 3. Ordenar os dados alfabeticamente pelo nome da empresa
values_sorted = sorted(values, key=lambda x: unidecode(x['Nome da Empresa'].lower()))

# 4. Remover duplicatas de URL, mantendo apenas a primeira ocorrência
unique_values = []
seen_urls = set()
for item in values_sorted:
    if item['URL'] not in seen_urls:
        seen_urls.add(item['URL'])
        unique_values.append(item)
values_sorted = unique_values

# 5. Salvar os dados ordenados no list.csv
save_sorted_csv(LIST_FILE_PATH, values_sorted, fieldnames=values_sorted[0].keys())

# 6. Gerar a tabela em Markdown
markdown_table = generate_markdown_table(values_sorted)

# 7. Carregar o cabeçalho do arquivo Markdown
header_content = load_header(HEADER_FILE_PATH)

# 8. Atualizar o arquivo README.md
with open(README_FILE_PATH, 'w', encoding='utf-8') as readme_file:
    readme_file.write(f'{header_content}\n\n{markdown_table}')
