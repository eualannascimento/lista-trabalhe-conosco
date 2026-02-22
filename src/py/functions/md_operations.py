# md_operations.py

def generate_markdown_table(data):
    """Gera uma tabela em Markdown com links para as empresas."""
    table_md = '| Nome da Empresa (+ Link do Trabalhe Conosco) | Segmento | Última Vaga |\n'
    table_md += '| --- | --- | --- |\n'
    for row in data:
        name = row['Nome da Empresa']
        url = row['URL']
        segment = row.get('Segmento da Empresa', '')
        last_job = row.get('Data de Publicação', '')
        table_md += f"| [{name}]({url}) | {segment} | {last_job} |\n"
    return table_md

def load_header(file_path):
    """Carrega o conteúdo do cabeçalho do arquivo."""
    with open(file_path, 'r') as file:
        return file.read()