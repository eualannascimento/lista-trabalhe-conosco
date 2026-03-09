import requests
import sys

url = "https://html.duckduckgo.com/html/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}
data = {"q": "teste"}
try:
    r = requests.post(url, headers=headers, data=data)
    print("Status:", r.status_code)
except Exception as e:
    print("Error:", e)
