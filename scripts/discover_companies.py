import requests
import json
import csv
import re
from urllib.parse import urlparse

def get_existing_urls():
    existing = set()
    try:
        with open('src/data/input/list.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row['URL'].lower().replace('https://', '').replace('http://', '').strip('/')
                existing.add(url)
    except Exception as e:
        print(f"Error reading list: {e}")
    return existing

def discover_subdomains(domain_suffix):
    print(f"Querying HackerTarget for {domain_suffix}...")
    url = f"https://api.hackertarget.com/hostsearch/?q={domain_suffix}"
    subdomains = set()
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            lines = resp.text.split('\n')
            for line in lines:
                if ',' in line:
                    sub, ip = line.split(',', 1)
                    sub = sub.strip().lower()
                    if sub.endswith(domain_suffix) and sub != domain_suffix and sub != f'www.{domain_suffix}':
                        subdomains.add(sub)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Found {len(subdomains)} unique subdomains for {domain_suffix}")
    return subdomains

def main():
    existing = get_existing_urls()
    print(f"Loaded {len(existing)} existing URLs.")
    
    new_candidates = []
    
    gupy_subs = discover_subdomains('gupy.io')
    for sub in gupy_subs:
        if sub not in existing and 'portal.api' not in sub and 'homolog' not in sub and 'beta' not in sub:
            company_name = sub.replace('.gupy.io', '').capitalize()
            new_candidates.append({
                'Nome da Empresa': company_name,
                'Segmento da Empresa': 'A Classificar',
                'Plataforma': 'Gupy',
                'URL': f"https://{sub}"
            })
            
    inhire_subs = discover_subdomains('inhire.com.br')
    for sub in inhire_subs:
        if sub not in existing and 'vagas.' not in sub and 'app.' not in sub:
            company_name = sub.replace('.inhire.com.br', '').capitalize()
            new_candidates.append({
                'Nome da Empresa': company_name,
                'Segmento da Empresa': 'A Classificar',
                'Plataforma': 'Inhire',
                'URL': f"https://{sub}"
            })

    print(f"Identified {len(new_candidates)} NEW candidates.")
    
    if new_candidates:
        fields = ["Nome da Empresa", "Segmento da Empresa", "Plataforma", "URL"]
        with open('src/data/input/new_items.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            f.seek(0, 2)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerows(new_candidates)
        print("Candidates appended to new_items.csv")

if __name__ == '__main__':
    main()

