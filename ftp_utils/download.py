from ftplib import FTP

ftp_server = input("Enter FTP server address: ")
username = input("Enter username: ")
password = input("Enter password: ")
filename = input("Enter filename to download: ")

ftp = FTP(ftp_server)
ftp.login(username, password)

print("Files on server:")
print(ftp.nlst())  

with open(filename, 'wb') as f:
    ftp.retrbinary(f'RETR {filename}', f.write)

ftp.quit()