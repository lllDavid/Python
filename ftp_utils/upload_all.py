import os
from ftplib import FTP

ftp = FTP(input("Host: "))
ftp.login(input("User: "), input("Pass: "))
local = input("Local dir: ").strip('"')
remote = input("Remote dir (or leave blank): ").strip()
overwrite = input("Overwrite existing? (y/n): ").lower() == 'y'

if remote: ftp.cwd(remote)
remote_files = ftp.nlst()

for f in os.listdir(local):
    path = os.path.join(local, f)
    if not os.path.isfile(path): continue
    if f in remote_files and not overwrite:
        print(f"Skip: {f}")
        continue
    if f in remote_files and overwrite:
        ftp.delete(f)
    with open(path, 'rb') as file:
        ftp.storbinary(f'STOR {f}', file)
        print(f"Uploaded: {f}")

ftp.quit()