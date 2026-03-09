import csv
import subprocess
import io

# Get current list
current_rows = []
with open('src/data/input/list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    current_header = next(reader)
    current_rows = list(reader)

# Get old list from commit 10cdf0a
result = subprocess.run(['git', 'show', '10cdf0a:src/data/input/list.csv'], capture_output=True, text=True)
old_csv_content = result.stdout
old_reader = csv.reader(io.StringIO(old_csv_content))
old_header = next(old_reader)
old_rows = list(old_reader)

old_company_map = {}
for row in old_rows:
    if len(row) > 5:
        name = row[2].strip().lower()
        url = row[5].strip()
        old_company_map[name] = url

# Count current vagas urls
vagas_prefix = "https://trabalheconosco.vagas.com.br/"
to_fix = []
for i, row in enumerate(current_rows):
    if len(row) > 5:
        url = row[5].strip()
        if url.startswith(vagas_prefix):
            name = row[2].strip().lower()
            old_url = old_company_map.get(name)
            if old_url and old_url != url:
                to_fix.append((i, row[2], url, old_url))
            elif not old_url:
                to_fix.append((i, row[2], url, "NOT_FOUND_IN_OLD"))

print(f"Total current URLs starting with {vagas_prefix}: {sum(1 for r in current_rows if len(r)>5 and r[5].startswith(vagas_prefix))}")
print(f"Number of URLs that are different from commit 10cdf0a or not found: {len(to_fix)}")

for item in to_fix[:20]:
    print(f"[{item[0]}] {item[1]}: Current={item[2]} | Old={item[3]}")
