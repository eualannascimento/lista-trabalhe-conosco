# md_operations.py

def generate_markdown_table(data):
    """Gera uma tabela em Markdown com links para as empresas."""
    table_md = '| Nome da Empresa (+ Link do Trabalhe Conosco) |\n'
    table_md += '| --- |\n'
    for row in data:
        table_md += f"| [{row['Nome da Empresa']}]({row['URL']}) |\n"
    return table_md

def load_header(file_path):
    """Carrega o conteúdo do cabeçalho do arquivo."""
    with open(file_path, 'r') as file:
        return file.read()