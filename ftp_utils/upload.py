from ftplib import FTP

ftp = FTP('ftp.example.com')
ftp.login('username', 'password')

filename = 'upload.txt'

with open(filename, 'rb') as f:
    ftp.storbinary(f'STOR {filename}', f)

ftp.quit()
