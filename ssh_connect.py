import subprocess

# Define server and user information
hostname = 'your.server.com'  # Replace with your server's hostname or IP address
username = 'your_username'      # Replace with your SSH username

# Construct the SSH command
ssh_command = f"ssh {username}@{hostname}"

try:
    # Execute the SSH command
    subprocess.run(ssh_command, shell=True)
except Exception as e:
    print(f"Failed to execute SSH command: {e}")
