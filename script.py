import csv
from unidecode import unidecode

# Abra o arquivo 'data/companies.csv' e armazene os valores em uma lista
with open('data/companies.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    values = [row for row in reader]

# Ordene os valores em ordem alfabética pela 'Empresa'
values_sorted = sorted(values, key=lambda x: unidecode(x['Empresa'].lower()))

# Atualize o arquivo 'data/companies.csv' com os valores em ordem alfabética pela 'Empresa'
with open('data/companies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=values_sorted[0].keys())
    writer.writeheader()
    writer.writerows(values_sorted)

# Abra o arquivo 'data/header.md'
with open('data/header.md', 'r') as file:
    header = file.read()

# Crie uma nova lista com as informações da tabela já formatadas como Markdown
table_md = '| Empresa (+ Link do Trabalhe Conosco) |\n'
table_md += '| --- |\n'
for row in values_sorted:
    table_md += f"| [{row['Empresa']}]({row['Site']}) |\n"

# Atualize o arquivo README.md
with open('README.md', 'w') as file:
    file.write(f'{header}\n\n{table_md}')