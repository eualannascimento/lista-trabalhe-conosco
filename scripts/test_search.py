import requests
from bs4 import BeautifulSoup

def search_ecosia(query):
    try:
        url = "https://www.ecosia.org/search"
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"q": query}
        r = requests.get(url, headers=headers, params=params, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        res = []
        for a in soup.find_all('a', class_='result-url'):
            res.append(a.get('href'))
        return res
    except Exception as e:
        return []

def search_brave(query):
    try:
        url = "https://search.brave.com/search"
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"q": query}
        r = requests.get(url, headers=headers, params=params, timeout=5)
        soup = BeautifulSoup(r.text, 'html.parser')
        res = []
        for a in soup.select('.result-header'):
            if a.get('href'):
                res.append(a.get('href'))
        return res
    except Exception as e:
        return []

print("Ecosia:", search_ecosia("Accenture trabalhe conosco"))
print("Brave:", search_brave("Accenture trabalhe conosco"))
