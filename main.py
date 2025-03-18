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

print("=== Itens encontrados no new_items.csv ===")
for item in new_items:
    print(item)

if new_items:
    # Lê todos os itens já presentes no list.csv
    existing_items = read_csv(LIST_FILE_PATH)
    # Cria um conjunto com as URLs já existentes (após limpeza)
    existing_urls = set(clean_url(item['URL']) for item in existing_items)
    new_entries_added = False
    new_items_duplicates = []  # Armazena itens duplicados em relação a list.csv

    for item in new_items:
        cleaned_url = clean_url(item['URL'])
        if cleaned_url in existing_urls:
            new_items_duplicates.append(item)
            continue
        # Prepara nova linha com os campos extras
        new_row = {
            'Status da URL': '0',
            'Data de Entrada': date.today().strftime("%Y-%m-%d"),
            'Nome da Empresa': item['Nome da Empresa'],
            'Segmento da Empresa': item['Segmento da Empresa'],
            'Plataforma': item['Plataforma'],
            'URL': cleaned_url
        }
        existing_items.append(new_row)
        existing_urls.add(cleaned_url)
        new_entries_added = True

    print("\n=== Itens duplicados no new_items.csv em relação a list.csv ===")
    if new_items_duplicates:
        for dup in new_items_duplicates:
            print(dup)
    else:
        print("Nenhum item duplicado encontrado no new_items.csv em relação a list.csv.")

    if new_entries_added:
        # Define a ordem dos campos para list.csv (sem 'Data do Status')
        fieldnames_temp = [ 'Status da URL', 'Data de Entrada','Nome da Empresa', 'Segmento da Empresa', 'Plataforma', 'URL']
        save_sorted_csv(LIST_FILE_PATH, existing_items, fieldnames_temp)
    
    # Limpa o arquivo new_items.csv, mantendo apenas o cabeçalho
    with open(NEW_ITEMS_FILE, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=['Nome da Empresa', 'Segmento da Empresa', 'Plataforma', 'URL'])
        writer.writeheader()

# %% 
# FLUXO PRINCIPAL
# 1. Ler e processar dados de list.csv
values = read_and_filter_csv(LIST_FILE_PATH)

# 2. Verificar status das URLs (atualiza para '1' se acessível ou mantém '0')
status_zero_items = []
for value in values:
    url = value['URL']
    status = verify_website_status(url)
    value['Status da URL'] = status
    # Adiciona o campo "Data do Status" temporariamente, mas ele será removido antes de salvar
    value['Data do Status'] = date.today().strftime("%Y-%m-%d")
    if status == '0':
        status_zero_items.append(value)

print("\n=== Itens com status '0' na verificação de URL ===")
if status_zero_items:
    for item in status_zero_items:
        print(item)
else:
    print("Todos os itens apresentaram status '1'.")

# 3. Ordenar os dados alfabeticamente pelo nome da empresa
values_sorted = sorted(values, key=lambda x: unidecode(x['Nome da Empresa'].lower()))

# 4. Remover duplicatas de URL, mantendo apenas a primeira ocorrência
unique_values = []
seen_urls = set()
duplicated_values = []  # Itens duplicados encontrados na lista completa

for item in values_sorted:
    if item['URL'] not in seen_urls:
        seen_urls.add(item['URL'])
        unique_values.append(item)
    else:
        duplicated_values.append(item)

print("\n=== Itens duplicados na lista completa (removidos) ===")
if duplicated_values:
    for dup in duplicated_values:
        print(dup)
else:
    print("Nenhum item duplicado encontrado na lista completa.")

values_sorted = unique_values

# 5. Remover o campo "Data do Status" de cada registro, conforme solicitado
for item in values_sorted:
    if 'Data do Status' in item:
        del item['Data do Status']

# 6. Salvar os dados ordenados no list.csv com a ordem desejada:
# Ordem: Status da URL, Data de Entrada, Nome da Empresa, Segmento da Empresa, Plataforma, URL
fieldnames = ['Status da URL', 'Data de Entrada', 'Nome da Empresa', 'Segmento da Empresa', 'Plataforma', 'URL']
save_sorted_csv(LIST_FILE_PATH, values_sorted, fieldnames=fieldnames)

# 7. Gerar a tabela em Markdown
markdown_table = generate_markdown_table(values_sorted)

# 8. Carregar o cabeçalho do arquivo Markdown
header_content = load_header(HEADER_FILE_PATH)

# 9. Atualizar o arquivo README.md
with open(README_FILE_PATH, 'w', encoding='utf-8') as readme_file:
    readme_file.write(f'{header_content}\n\n{markdown_table}')
