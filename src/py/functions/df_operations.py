# df_operations.py

def clean_url(url):
    """Remove trailing slashes or spaces from a URL."""
    return url.rstrip('/ ').strip()