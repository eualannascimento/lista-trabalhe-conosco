import requests
import urllib3

urllib3.disable_warnings()

def is_valid_gupy(name):
    # Test both variants
    for url in [f"https://{name}.gupy.io", f"https://carreiras.gupy.io/{name}"]:
        try:
            r = requests.get(url, timeout=3, allow_redirects=False, verify=False)
            # If valid, Gupy returns 200 directly. 
            # If invalid, Gupy returns 302 or 301 or 404.
            if r.status_code == 200:
                return url
        except Exception:
            pass
    return None

def is_valid_kenoby(name):
    url = f"https://jobs.kenoby.com/{name}"
    try:
        r = requests.get(url, timeout=3, allow_redirects=False, verify=False)
        if r.status_code == 200:
            return url
    except Exception:
        pass
    return None

def is_valid_solides(name):
    url = f"https://{name}.solides.jobs"
    try:
        r = requests.get(url, timeout=3, allow_redirects=False, verify=False)
        if r.status_code == 200:
            return url
    except Exception:
        pass
    return None

print("accenture gupy:", is_valid_gupy("accenture"))
print("alberteinstein gupy:", is_valid_gupy("alberteinstein"))
print("einstein gupy:", is_valid_gupy("einstein"))
print("allos gupy:", is_valid_gupy("allos"))
print("fake gupy:", is_valid_gupy("fakename12345"))
