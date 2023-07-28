# Import modules
import csv
from unidecode import unidecode

# Open the file `src/csv/career-websites.csv` and store the active values in a list.
with open('src/csv/career-websites.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    values = []
    for row in reader:
        if row.get('Status da URL') == '1':
            values.append(row)

# Sort the values in alphabetical order by `Nome da Empresa`.
values_sorted = sorted(values, key=lambda x: unidecode(x['Nome da Empresa'].lower()))

# Update the file `src/csv/career-websites.csv with the values in alphabetical order by `Nome da Empresa`.
with open('src/csv/career-websites.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=values_sorted[0].keys())
    writer.writeheader()
    writer.writerows(values_sorted)

# Open the file `src/md/header.md`.
with open('src/md/header.md', 'r') as file:
    header = file.read()

# Create a new list with the table information already formatted as Markdown.
table_md = '| Nome da Empresa (+ Link do Trabalhe Conosco) |\n'
table_md += '| --- |\n'
for row in values_sorted:
    table_md += f"| [{row['Nome da Empresa']}]({row['URL']}) |\n"

# Update the file README.md.
with open('README.md', 'w') as file:
    file.write(f'{header}\n\n{table_md}')