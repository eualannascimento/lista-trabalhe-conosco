from urllib.parse import urlparse


def clean_url(url):
    """Remove espaços e barras finais de uma URL."""
    return url.strip().rstrip("/")


def validate_url(url):
    """
    Valida se uma URL tem formato válido.
    Retorna True se a URL tem scheme (http/https) e netloc válidos.
    """
    cleaned = clean_url(url)
    parsed = urlparse(cleaned)
    return bool(parsed.scheme in ("http", "https") and parsed.netloc)
