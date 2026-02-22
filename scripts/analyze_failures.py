import csv
import requests
import urllib3
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5, verify=False, allow_redirects=True)
        return (url, f"HTTP {resp.status_code}")
    except requests.exceptions.ConnectionError as e:
        if "NameResolutionError" in str(e) or "getaddrinfo" in str(e):
            return (url, "DNS Resolution Error (Site offline)")
        return (url, "Connection Error")
    except requests.exceptions.Timeout:
        return (url, "Timeout")
    except Exception as e:
        return (url, f"Other Error: {type(e).__name__}")

def main():
    failed_urls = []
    with open('src/data/input/list.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Status da URL'] == '0':
                failed_urls.append(row['URL'])
    
    print(f"Total failed URLs to analyze: {len(failed_urls)}")
    
    results = []
    # Test a sample of 150 to get a good distribution without taking too long
    sample = failed_urls[:150]
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_url, url): url for url in sample}
        for future in as_completed(futures):
            results.append(future.result())
            
    # Tally up the errors
    error_counts = Counter(err for url, err in results)
    
    print("\n--- Error Breakdown ---")
    for err, count in error_counts.most_common():
        print(f"{err}: {count} ({count/len(sample)*100:.1f}%)")
        
    print("\n--- Example DNS Errors (Likely Dead) ---")
    dns = [u for u, e in results if "DNS" in e][:5]
    for d in dns: print(d)
        
    print("\n--- Example 404s (Page Removed) ---")
    err404 = [u for u, e in results if "404" in e][:5]
    for e in err404: print(e)

if __name__ == "__main__":
    main()
