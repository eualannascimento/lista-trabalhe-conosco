import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10
MAX_RETRIES = 2
RETRY_DELAY = 1
MAX_WORKERS = 20

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}


def _is_success(status_code):
    """Retorna True se o status HTTP indica sucesso (2xx ou 3xx)."""
    return 200 <= status_code < 400


def verify_website_status(url, timeout=DEFAULT_TIMEOUT, retries=MAX_RETRIES):
    """
    Verifica se um website está acessível via requisição GET.
    Aceita status HTTP 2xx e 3xx como sucesso.
    Retorna um dict com 'status' ('1' ou '0'), 'status_code', e 'error'.
    """
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                url,
                timeout=timeout,
                headers=HEADERS,
                allow_redirects=True,
                verify=True,
            )
            if _is_success(response.status_code):
                logger.debug("OK  | %s | HTTP %d", url, response.status_code)
                return {"status": "1", "status_code": response.status_code, "error": None}
            else:
                last_error = f"HTTP {response.status_code}"
                logger.debug(
                    "FALHA | %s | HTTP %d (tentativa %d/%d)",
                    url, response.status_code, attempt, retries,
                )
        except RequestException as e:
            last_error = str(e)
            logger.debug(
                "ERRO  | %s | %s (tentativa %d/%d)",
                url, last_error, attempt, retries,
            )

        if attempt < retries:
            time.sleep(RETRY_DELAY * attempt)

    # Tenta sem verificação SSL como fallback
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers=HEADERS,
            allow_redirects=True,
            verify=False,
        )
        if _is_success(response.status_code):
            logger.debug("OK (sem SSL) | %s | HTTP %d", url, response.status_code)
            return {"status": "1", "status_code": response.status_code, "error": None}
        else:
            last_error = f"HTTP {response.status_code}"
    except RequestException as e:
        last_error = str(e)

    logger.info("FALHA | %s | %s", url, last_error)
    return {"status": "0", "status_code": None, "error": last_error}


def verify_websites_concurrent(items, timeout=DEFAULT_TIMEOUT, max_workers=MAX_WORKERS):
    """
    Verifica uma lista de itens concorrentemente.
    Cada item deve ser um dict com pelo menos as chaves 'URL' e 'Nome da Empresa'.
    Atualiza 'Status da URL' em cada item e retorna a lista de itens com status '0'.
    """
    failed_items = []
    total = len(items)

    logger.info("Iniciando verificação de %d URLs com %d workers...", total, max_workers)

    def _check(item):
        url = item["URL"]
        result = verify_website_status(url, timeout=timeout)
        return item, result

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_check, item): item for item in items}
        done_count = 0

        for future in as_completed(futures):
            done_count += 1
            item, result = future.result()
            item["Status da URL"] = result["status"]

            if result["status"] == "0":
                item["_error"] = result["error"]
                failed_items.append(item)

            if done_count % 50 == 0 or done_count == total:
                logger.info("Progresso: %d/%d URLs verificadas", done_count, total)

    logger.info(
        "Verificação concluída: %d/%d URLs acessíveis, %d falhas",
        total - len(failed_items), total, len(failed_items),
    )
    return failed_items
