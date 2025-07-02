from ftplib import FTP

ftp_server = input("Enter FTP server address: ")
username = input("Enter username: ")
password = input("Enter password: ")
filename = input("Enter filename to upload: ")

ftp = FTP(ftp_server)
ftp.login(username, password)

with open(filename, 'rb') as f:
    ftp.storbinary(f'STOR {filename}', f)

ftp.quit()