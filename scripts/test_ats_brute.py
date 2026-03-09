import requests
import urllib3

urllib3.disable_warnings()

def test_ats(company_name):
    clean_name = ''.join(c for c in company_name.lower() if c.isalnum() or c == ' ').strip().replace(' ', '')
    clean_name_dash = ''.join(c for c in company_name.lower() if c.isalnum() or c == ' ').strip().replace(' ', '-')
    
    candidates = [
        f"https://{clean_name}.gupy.io",
        f"https://carreiras.gupy.io/{clean_name}",
        f"https://{clean_name_dash}.gupy.io",
        f"https://jobs.kenoby.com/{clean_name}",
        f"https://jobs.kenoby.com/{clean_name_dash}",
        f"https://{clean_name}.solides.jobs",
        f"https://{clean_name_dash}.solides.jobs",
        f"https://{clean_name}.empregare.com/pt-br",
        f"https://www.vagas.com.br/vagas-de-{clean_name}",
        f"https://www.vagas.com.br/vagas-de-{clean_name_dash}"
    ]
    
    headers = {"User-Agent": "Mozilla/5.0"}
    session = requests.Session()
    session.headers.update(headers)
    
    for url in candidates:
        try:
            r = session.get(url, timeout=3, allow_redirects=True, verify=False)
            if 200 <= r.status_code < 400:
                if "portal.gupy.io" not in r.url and "notfound" not in r.url.lower():
                    return r.url
        except Exception as e:
            pass
            
    return None

print("Accenture ->", test_ats("Accenture"))
print("Aché Laboratórios ->", test_ats("Aché Laboratórios"))
print("Allos ->", test_ats("Allos"))
