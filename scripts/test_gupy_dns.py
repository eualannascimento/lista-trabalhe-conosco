import requests

def test_gupy(name):
    url = f"https://{name}.gupy.io"
    try:
        r = requests.get(url, timeout=3)
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False
    except Exception:
        return False

print("allos:", test_gupy("allos"))
print("accenture:", test_gupy("accenture"))
print("alberteinstein:", test_gupy("alberteinstein"))
print("einstein:", test_gupy("einstein"))
print("fakename1234:", test_gupy("fakename1234"))
