import requests

def test_sql_injection(url):
    payload = "' OR '1'='1"  
    response = requests.get(url, params={'id': payload})
    if "error" not in response.text.lower():
        print(f"Potential SQL Injection vulnerability found at {url}")
    else:
        print(f"No SQL Injection vulnerability found at {url}")

if __name__ == "__main__":
    target_url = "http://127.0.0.1/vulnerable_page"  
    test_sql_injection(target_url)

