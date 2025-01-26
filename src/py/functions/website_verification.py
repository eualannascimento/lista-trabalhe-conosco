import requests
import urllib.request
import urllib.error
import socket
from requests.exceptions import RequestException  # Import explícito

def verify_website_status(url):
    """
    Verifica o status de um website tentando métodos GET, POST e urllib.
    Retorna '1' se o website está acessível (HTTP 200), caso contrário '0'.
    """
    try:
        # Tenta uma requisição GET
        response = requests.get(url)
        if response.status_code == 200:
            return '1'
    except RequestException:  # Uso direto de RequestException
        # Tenta uma requisição POST caso GET falhe
        try:
            response = requests.post(url)
            if response.status_code == 200:
                return '1'
        except RequestException:
            # Tenta urllib caso POST falhe
            try:
                response = urllib.request.urlopen(url)
                if response.getcode() == 200:
                    return '1'
            except (urllib.error.URLError, socket.gaierror):
                pass  # Captura erros de conexão
    # Se nenhuma tentativa deu certo, retorna '0'
    return '0'
