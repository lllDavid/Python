import subprocess

hostname = ''  
username = ''      

ssh_command = f"ssh {username}@{hostname}"

try:
    subprocess.run(ssh_command, shell=True)
except Exception as e:
    print(f"Failed to execute SSH command: {e}")
