import csv
import time
import asyncio
from urllib.parse import urlparse, urlunparse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

def clean_url(url):
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

async def scrape_bing(page, company_name):
    query = f"{company_name} trabalhe conosco carreiras"
    url = f"https://www.bing.com/search?q={query}"
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=10000)
        # Give JS a second to render
        await page.wait_for_timeout(1000)
        
        # Parse output
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')
        
        for li in soup.find_all('li', class_='b_algo'):
            a = li.find('a')
            if a and a.get('href'):
                link = a['href']
                if ('gupy' in link or 'jobs' in link or 'carreiras' in link or 'trabalhe' in link or 'solides' in link or 'kenoby' in link) and ('linkedin.com' not in link and 'glassdoor' not in link and 'infojobs' not in link):
                    return clean_url(link)
                
        # Fallback to first non-bing link
        for li in soup.find_all('li', class_='b_algo'):
            a = li.find('a')
            if a and a.get('href'):
                link = a['href']
                if 'bing.com' not in link:
                    return clean_url(link)
    except Exception as e:
        print(f"Error on {company_name}: {e}")
    return None

async def main():
    vagas_prefix = "https://trabalheconosco.vagas.com.br/"
    
    # 1. Read CSV
    all_rows = []
    with open('src/data/input/list.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        all_rows = list(reader)
        
    targets = []
    for row in all_rows:
         if len(row) > 5 and row[5].strip().startswith(vagas_prefix):
             name = row[2].strip()
             targets.append((row, name))
             
    print(f"Alvos para buscar na web via Playwright: {len(targets)}")
    
    new_urls_map = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        done = 0
        for row, name in targets:
            url = await scrape_bing(page, name)
            if url:
                new_urls_map[name] = url
            done += 1
            if done % 10 == 0:
                print(f"Progresso: {done}/{len(targets)}...")
            
        await browser.close()
        
    print(f"Recuperou {len(new_urls_map)} novas URLs da web.")
    
    # Update CSV
    updated_rows = []
    for row in all_rows:
        if len(row) > 5:
            name = row[2].strip()
            if name in new_urls_map and row[5].strip().startswith(vagas_prefix):
                row[5] = new_urls_map[name]
        updated_rows.append(row)
        
    with open('src/data/input/list.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(updated_rows)
        
    print("CSV Atualizado com sucesso!")

if __name__ == "__main__":
    asyncio.run(main())
