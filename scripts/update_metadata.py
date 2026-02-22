import csv
import requests
import re
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_gupy_date(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200: return None
        
        # Extract buildId and first jobId
        build_match = re.search(r'\"buildId\":\"(.*?)\"', resp.text)
        job_match = re.search(r'\"id\":(\d{7,10})', resp.text)
        
        if build_match and job_match:
            build_id = build_match.group(1)
            job_id = job_match.group(1)
            detail_url = f"{url.rstrip('/')}/_next/data/{build_id}/pt/jobs/{job_id}.json"
            detail_resp = requests.get(detail_url, headers=headers, timeout=10)
            if detail_resp.status_code == 200:
                data = detail_resp.json()
                date_str = data.get('pageProps', {}).get('job', {}).get('publishedAt')
                if date_str:
                    return date_str[:10] # YYYY-MM-DD
    except:
        pass
    return None

def get_vagas_date(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        # Try the opportunities page
        opp_url = url.rstrip('/') + "/oportunidades"
        resp = requests.get(opp_url, headers=headers, timeout=10)
        if resp.status_code != 200:
             resp = requests.get(url, headers=headers, timeout=10)
        
        # Look for dates like DD/MM/YYYY
        dates = re.findall(r'\d{2}/\d{2}/\d{4}', resp.text)
        if dates:
            # Return the most recent one (naive but often works)
            # Reformat to YYYY-MM-DD for consistency
            d, m, y = dates[0].split('/')
            return f"{y}-{m}-{d}"
    except:
        pass
    return None

def update_row(row):
    p = row.get('Plataforma')
    url = row.get('URL')
    if row.get('Data de Publicação'): return row # Skip already updated
    
    date = None
    if p == 'Gupy':
        date = get_gupy_date(url)
    elif p == 'Vagas':
        date = get_vagas_date(url)
    
    if date:
        row['Data de Publicação'] = date
    return row

def main():
    path = 'src/data/input/list.csv'
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    print(f"Updating metadata for {len(rows)} companies...")
    
    # Process only a subset for testing first 100 Gupy/Vagas
    to_update = [r for r in rows if r.get('Plataforma') in ['Gupy', 'Vagas'] and not r.get('Data de Publicação')]
    print(f"Candidates for update: {len(to_update)}")
    
    updated_rows = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(update_row, row): row for row in to_update}
        for future in as_completed(futures):
            updated_rows.append(future.result())
            if len(updated_rows) % 50 == 0 or len(updated_rows) == len(to_update):
                print(f"Progress: {len(updated_rows)}/{len(to_update)}")

    # Merge back
    update_map = {r['URL']: r['Data de Publicação'] for r in updated_rows}
    for row in rows:
        if row['URL'] in update_map:
            row['Data de Publicação'] = update_map[row['URL']]

    # Save
    fieldnames = list(rows[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("Metadata update complete for sample batch.")

if __name__ == "__main__":
    main()
