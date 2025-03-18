# %% 
import requests
import urllib.request
import urllib.error
import socket
from requests.exceptions import RequestException

def verify_website_status(url):
    """
    Verifica se um website está acessível tentando métodos GET, POST e urllib.
    Retorna '1' se o site retornar status HTTP 200, caso contrário '0'.
    """
    timeout = 5  # tempo limite em segundos para as requisições

    # Tenta uma requisição GET
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return '1'
    except RequestException:
        pass

    # Tenta uma requisição POST se GET não for bem-sucedida
    try:
        response = requests.post(url, timeout=timeout)
        if response.status_code == 200:
            return '1'
    except RequestException:
        pass

    # Tenta usar urllib como última alternativa
    try:
        response = urllib.request.urlopen(url, timeout=timeout)
        if response.getcode() == 200:
            return '1'
    except (urllib.error.URLError, socket.gaierror):
        pass

    # Se nenhuma das tentativas obtiver sucesso, retorna '0'
    return '0'