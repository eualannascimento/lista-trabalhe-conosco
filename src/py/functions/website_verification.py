import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.exceptions import RequestException, SSLError, Timeout

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 15  # Increased timeout
MAX_RETRIES = 2
RETRY_DELAY = 1.5
MAX_WORKERS = 15  # Slightly reduced to avoid congestion

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

def verify_website_status(url, timeout=DEFAULT_TIMEOUT, retries=MAX_RETRIES):
    """
    Verifica se um website está acessível.
    Tenta lidar com erros comuns como Timeouts e SSL de forma graciosa.
    Retorna dict com status ('1' ou '0'), status_code e mensagem de erro.
    """
    last_error = None
    
    # Padronização da URL (se necessário)
    if not url.startswith("http"):
        url = "https://" + url

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                url,
                timeout=timeout,
                headers=HEADERS,
                allow_redirects=True, # Seguir redirects é crucial
                verify=True,
            )
            
            # Checagem de sucesso
            if 200 <= response.status_code < 400:
                # Opcional: checar por "soft 404" ou páginas de erro customizadas
                # Mas por enquanto, status code é o indicador primário.
                return {"status": "1", "status_code": response.status_code, "error": None}
            elif response.status_code == 403:
                # 403 muitas vezes é bloqueio de bot, mas o site existe.
                # Se for 403, podemos considerar "Incerto" ou "1" com aviso?
                # Regra segura: Se respondeu 403, o servidor existe.
                # Mas para candidatura, se não conseguimos acessar, é falha?
                # Vamos manter como falha de validação automática por enquanto.
                last_error = f"HTTP {response.status_code} (Acesso Negado)"
            elif response.status_code == 404:
                last_error = f"HTTP {response.status_code} (Não Encontrado)"
            else:
                last_error = f"HTTP {response.status_code}"

        except SSLError:
            last_error = "Erro SSL/Certificado"
            # Tenta sem verificar SSL na próxima tentativa ou logo abaixo
            try:
                response = requests.get(
                    url, timeout=timeout, headers=HEADERS, allow_redirects=True, verify=False
                )
                if 200 <= response.status_code < 400:
                     return {"status": "1", "status_code": response.status_code, "error": "Sucesso (SSL Ignorado)"}
            except Exception as e:
                last_error = f"Erro SSL + Falha sem SSL: {str(e)}"

        except Timeout:
            last_error = "Timeout (Tempo limite excedido)"
        except RequestException as e:
            last_error = f"Erro de Conexão: {str(e)}"
        except Exception as e:
            last_error = f"Erro Desconhecido: {str(e)}"

        # Espera antes de tentar novamente (backoff)
        if attempt < retries:
            time.sleep(RETRY_DELAY * attempt)

    logger.warning("FALHA FINAL | %s | %s", url, last_error)
    return {"status": "0", "status_code": None, "error": last_error}


def verify_websites_concurrent(items, timeout=DEFAULT_TIMEOUT, max_workers=MAX_WORKERS):
    """
    Verifica URLs em paralelo.
    Retorna failed_items: Lista de dicionários das empresas que falharam.
    Cada item modificado ganha 'Status da URL' e '_error'.
    """
    failed_items = []
    total = len(items)

    logger.info("Iniciando verificação robusta de %d URLs...", total)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Map future -> item
        futures = {executor.submit(verify_website_status, item["URL"], timeout): item for item in items}
        
        done_count = 0
        for future in as_completed(futures):
            item = futures[future]
            done_count += 1
            
            try:
                result = future.result()
            except Exception as e:
                result = {"status": "0", "status_code": None, "error": f"Exception no worker: {str(e)}"}
            
            # Atualiza o item original
            item["Status da URL"] = result["status"]
            
            if result["status"] == "0":
                item["_error"] = result.get("error", "Erro não especificado")
                failed_items.append(item)
                # Log de progresso apenas para erros para não poluir
                logger.debug("Falha em %s: %s", item["Nome da Empresa"], item["_error"])
            else:
                item.pop("_error", None) # Limpa erro anterior se existir

            if done_count % 20 == 0 or done_count == total:
                 logger.info("Progresso: %d/%d verificados...", done_count, total)

    return failed_items
