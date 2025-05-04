import subprocess
import logging

logging.basicConfig(filename='ssh_log.txt', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def ssh_connect_and_log(host, username, command):
    try:
        ssh_command = ['ssh', f'{username}@{host}', command]
        
        logging.info(f'Connecting to {host} as {username}...')
        result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)

        logging.info(f'Command output: {result.stdout.strip()}')
    
    except subprocess.CalledProcessError as e:
        logging.error(f'Error occurred: {e.stderr.strip()}')
    
    except Exception as e:
        logging.error(f'Unexpected error: {e}')

if __name__ == "__main__":
    HOST = ''
    USERNAME = ''
    COMMAND = 'uptime'

    ssh_connect_and_log(HOST, USERNAME, COMMAND)
