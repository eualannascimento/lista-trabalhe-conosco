import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException, SSLError, Timeout
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10  # Reduced timeout, TCP is faster with Keep-Alive
MAX_RETRIES = 2
RETRY_DELAY = 1.0
MAX_WORKERS = 15

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

def create_shared_session():
    """Cria uma sessão global otimizada com Keep-Alive."""
    session = requests.Session()
    # HTTPAdapter increases connection pool size (number of parallel Keep-Alive connections)
    # Using a larger pool size than MAX_WORKERS prevents thread starvation
    adapter = HTTPAdapter(pool_connections=MAX_WORKERS, pool_maxsize=MAX_WORKERS * 2)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(HEADERS)
    return session

def _check_status(status_code):
    return 200 <= status_code < 400 or status_code == 403 or status_code == 408

def verify_website_status(session, url, timeout=DEFAULT_TIMEOUT, retries=MAX_RETRIES):
    """
    Verifica se um website está acessível usando Head e Fallback para Get.
    """
    last_error = None
    
    if not url.startswith("http"):
        url = "https://" + url

    for attempt in range(1, retries + 1):
        try:
            # 1. Tentar HEAD primeiro para economizar banda (só headers)
            response = session.head(
                url,
                timeout=timeout,
                allow_redirects=True,
                verify=True,
            )
            
            # Alguns servidores bloqueiam HEAD (405 Method Not Allowed) ou Bot Protect
            if _check_status(response.status_code):
                return {"status": "1", "status_code": response.status_code, "error": None}
            elif response.status_code == 405 or response.status_code == 401 or response.status_code == 501:
                # Fallback mandatário
                pass
            elif response.status_code == 404:
                if not url.endswith('/'):
                    try:
                        resp_slash = session.head(url + '/', timeout=timeout, allow_redirects=True)
                        if _check_status(resp_slash.status_code):
                            return {"status": "1", "status_code": resp_slash.status_code, "error": None}
                    except:
                        pass
                last_error = f"HTTP {response.status_code} (Não Encontrado)"
                # Se for 404, não adianta tentar GET
                continue
                
            # 2. Fallback para GET se o HEAD for bloqueado explicitamente (405/Bot block bizarro)
            response = session.get(url, timeout=timeout, allow_redirects=True, verify=True)
            if _check_status(response.status_code):
                return {"status": "1", "status_code": response.status_code, "error": None}
            elif response.status_code == 404:
                last_error = f"HTTP {response.status_code} (Não Encontrado)"
            else:
                 last_error = f"HTTP {response.status_code}"

        except SSLError:
            return {"status": "1", "status_code": None, "error": "Sucesso (Bloqueio SSL / Proteção Bot)"}
        except Timeout:
            return {"status": "1", "status_code": None, "error": "Sucesso (Timeout / Proteção Bot)"}
        except RequestException as e:
            last_error = f"Erro de Conexão: {str(e)}"
        except Exception as e:
            last_error = f"Erro Desconhecido: {str(e)}"

        if attempt < retries:
            time.sleep(RETRY_DELAY * attempt)

    logger.warning("FALHA FINAL | %s | %s", url, last_error)
    return {"status": "0", "status_code": None, "error": last_error}


def verify_websites_concurrent(items, timeout=DEFAULT_TIMEOUT, max_workers=MAX_WORKERS):
    """Verifica URLs em paralelo reutilizando conexões."""
    failed_items = []
    total = len(items)

    logger.info("Iniciando verificação robusta de %d URLs (Keep-Alive)...", total)
    
    # Criar uma unica sessao compartilhada por todas as threads para conexoes persistentes
    global_session = create_shared_session()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(verify_website_status, global_session, item["URL"], timeout): item for item in items}
        
        done_count = 0
        for future in as_completed(futures):
            item = futures[future]
            done_count += 1
            
            try:
                result = future.result()
            except Exception as e:
                result = {"status": "0", "status_code": None, "error": f"Exception no worker: {str(e)}"}
            
            item["Status da URL"] = result["status"]
            
            if result["status"] == "0":
                item["_error"] = result.get("error", "Erro não especificado")
                failed_items.append(item)
                logger.debug("Falha em %s: %s", item["Nome da Empresa"], item["_error"])
            else:
                item.pop("_error", None)

            if done_count % 50 == 0 or done_count == total:
                 logger.info("Progresso: %d/%d verificados...", done_count, total)

    return failed_items
