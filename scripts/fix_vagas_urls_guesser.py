import csv
import requests
import urllib3
import concurrent.futures

urllib3.disable_warnings()

def is_valid_ats(company_name):
    # Prepare permutations
    c1 = ''.join(c for c in company_name.lower() if c.isalnum() or c == ' ').strip().replace(' ', '')
    c2 = ''.join(c for c in company_name.lower() if c.isalnum() or c == ' ').strip().replace(' ', '-')
    c3 = c1.split('s/a')[0].split('ltda')[0].strip() # remove S/A or LTDA
    
    bases = list(set([c1, c2, c3]))
    candidates = []
    for b in bases:
        if not b: continue
        candidates.extend([
            f"https://{b}.gupy.io",
            f"https://carreiras.gupy.io/{b}",
            f"https://jobs.kenoby.com/{b}",
            f"https://{b}.solides.jobs",
            f"https://{b}.empregare.com/pt-br"
        ])
        
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    
    for url in candidates:
        try:
            r = session.get(url, timeout=4, allow_redirects=True, verify=False)
            if 200 <= r.status_code < 400:
                final = r.url.lower().rstrip('/')
                
                # Exclude generic Gupy portals
                if final == "https://carreiras.gupy.io" or final == "https://portal.gupy.io" or "portal.gupy.io" in final:
                    continue
                # Exclude Kenoby generic
                if "kenoby.com" in final and "jobs.kenoby.com" not in final:
                    continue
                # Exclude Solides generic
                if "solides.jobs" in final and "notfound" in final:
                    continue
                    
                return final
        except Exception:
            pass
            
    return None

if __name__ == "__main__":
    vagas_prefix = "https://trabalheconosco.vagas.com.br/"
    
    all_rows = []
    with open('src/data/input/list.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        all_rows = list(reader)
        
    # Get unique sets of companies that ONLY have the vagas URL
    targets = {}
    for row in all_rows:
        if len(row) > 5:
            name = row[2].strip()
            url = row[5].strip()
            if name not in targets:
                targets[name] = []
            targets[name].append(url)
            
    real_targets = []
    for name, urls in targets.items():
        if all(u.startswith(vagas_prefix) for u in urls):
            real_targets.append(name)
            
    print(f"Buscando domínios para {len(real_targets)} empresas...")
    
    new_urls_map = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_name = {executor.submit(is_valid_ats, name): name for name in real_targets}
        done = 0
        for future in concurrent.futures.as_completed(future_to_name):
            name = future_to_name[future]
            try:
                url = future.result()
                if url:
                    new_urls_map[name] = url
            except Exception as e:
                pass
            done += 1
            if done % 20 == 0:
                print(f"Progresso: {done}/{len(real_targets)}...")

    print(f"SUCESSO! O Guesser determinístico achou {len(new_urls_map)} de {len(real_targets)}.")
    missing = [name for name in real_targets if name not in new_urls_map]
    print(f"FALTAM {len(missing)} EMPRESAS! Salvando 'missing.txt' para pesquisa manual.")
    with open('missing.txt', 'w') as f:
        for m in missing:
            f.write(m + "\n")
            
    # Update CSV
    updated_rows = []
    for row in all_rows:
        if len(row) > 5:
            name = row[2].strip()
            if name in new_urls_map and row[5].strip().startswith(vagas_prefix):
                row[4] = "Gupy/Solides/Kenoby" # generic mapping
                row[5] = new_urls_map[name]
        updated_rows.append(row)
        
    with open('src/data/input/list.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(updated_rows)
        
    print("CSV Atualizado com os encontrados.")
