# %%
from src.py.functions.file_operations import read_and_filter_csv, save_sorted_csv
from src.py.functions.md_operations import generate_markdown_table, load_header
from src.py.functions.website_verification import verify_website_status
from unidecode import unidecode
from datetime import date

# Caminhos dos arquivos
CSV_FILE_PATH = 'src/data/input/list.csv'
HEADER_FILE_PATH = 'src/data/input/header.md'
README_FILE_PATH = 'README.md'

if __name__ == "__main__":
    # 1. Ler e filtrar dados
    values = read_and_filter_csv(CSV_FILE_PATH)

    # 2. Verificar status das URLs
    for value in values:
        url = value['URL']
        value['Status da URL'] = verify_website_status(url)
        value['Data do Status'] = date.today().strftime("%Y-%m-%d")

    # 3. Ordenar dados alfabeticamente pelo nome da empresa
    values_sorted = sorted(values, key=lambda x: unidecode(x['Nome da Empresa'].lower()))

    # 4. Salvar dados ordenados no CSV
    save_sorted_csv(CSV_FILE_PATH, values_sorted, fieldnames=values_sorted[0].keys())

    # 5. Gerar tabela em Markdown
    markdown_table = generate_markdown_table(values_sorted)

    # 6. Carregar cabeçalho do arquivo de Markdown
    header_content = load_header(HEADER_FILE_PATH)

    # 7. Atualizar o arquivo README.md
    with open(README_FILE_PATH, 'w') as readme_file:
        readme_file.write(f'{header_content}\n\n{markdown_table}')