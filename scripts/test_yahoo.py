import requests
from bs4 import BeautifulSoup

def search_yahoo(query):
    url = f"https://search.yahoo.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    params = {"p": query}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        # print("Status Yahoo:", response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        for div in soup.find_all('div', class_='compTitle'):
            a = div.find('a')
            if a and a.get('href'):
                link = a['href']
                if not "yahoo.com" in link:
                    results.append(link)
        return results
    except Exception as e:
        print(f"Erro: {e}")
        return []

if __name__ == "__main__":
    links = search_yahoo("Accenture trabalhe conosco carreiras")
    print(f"Resultados encontrados: {len(links)}")
    for l in links[:3]:
        print(l)
