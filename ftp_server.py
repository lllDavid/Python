import socket
import os
import sys

HOST = '127.0.0.1'
PORT = 21
DATA_PORT = 20
ROOT_DIR = './ftp_root'
USERNAME = 'user'
PASSWORD = 'pass'

def send_response(client_sock, code, message):
    print(f"Sending: {code} {message}")
    client_sock.send(f"{code} {message}\r\n".encode())

def initialize_ftp_root():
    try:
        root_dir_abs = os.path.abspath(ROOT_DIR)
        if os.path.exists(root_dir_abs):
            print(f"Directory already exists: {root_dir_abs}")
            if not os.access(root_dir_abs, os.W_OK):
                print(f"Error: Directory {root_dir_abs} is not writable")
                return False
        else:
            os.makedirs(root_dir_abs, exist_ok=True)
            print(f"Created directory: {root_dir_abs}")

        test_files = ['test1.txt', 'test2.txt', 'test3.txt']
        for file_name in test_files:
            file_path = os.path.join(root_dir_abs, file_name)
            if not os.path.exists(file_path):
                try:
                    with open(file_path, 'w') as f:
                        f.write(f"Sample content for {file_name}")
                    print(f"Created test file: {file_path}")
                except Exception as e:
                    print(f"Error: Failed to create {file_path}: {str(e)}")
                    return False
            else:
                print(f"Test file already exists: {file_path}")
        return True
    except PermissionError as e:
        print(f"Error: Permission denied when creating {root_dir_abs} or test files: {str(e)}")
        return False
    except Exception as e:
        print(f"Error: Failed to initialize {root_dir_abs} or test files: {str(e)}")
        return False

def handle_client(client_sock, client_addr):
    welcome_message = (
        "FTP Server ready\r\n"
        "Available commands:\r\n"
        "  ls - List files in current directory\r\n"
        "  dir - List files in current directory\r\n"
        "  put <filename> - Upload a file\r\n"
        "  get <filename> - Download a file\r\n"
        "  user <username> - Authenticate with username\r\n"
        "  quit - Exit the session\r\n"
        "  quote <command> - Send raw FTP command (e.g., NLST)"
    )
    send_response(client_sock, 220, welcome_message)
    authenticated = False
    current_dir = os.path.abspath(ROOT_DIR)  
    data_port = DATA_PORT  
    data_host = client_addr[0]  

    while True:
        try:
            data = client_sock.recv(1024).decode().strip()
            if not data:
                print("Client disconnected")
                break
            print(f"Raw received: '{data}'")
            command, *args = data.split(' ', 1)
            command = command.upper().strip()  
            args = args[0].strip() if args else ''
            print(f"Parsed: command='{command}', args='{args}'")

            match command:
                case 'USER':
                    if args == USERNAME:
                        send_response(client_sock, 331, "User name okay, need password")
                    else:
                        send_response(client_sock, 530, "Invalid username")
                
                case 'PASS':
                    if args == PASSWORD:
                        authenticated = True
                        send_response(client_sock, 230, "User logged in")
                    else:
                        send_response(client_sock, 530, "Invalid password")
                
                case 'QUIT':
                    send_response(client_sock, 221, "Goodbye")
                    break
                
                case 'PORT':
                    try:
                        parts = args.split(',')
                        if len(parts) != 6:
                            send_response(client_sock, 501, "Invalid PORT command")
                            continue
                        data_host = '.'.join(parts[:4])
                        data_port = int(parts[4]) * 256 + int(parts[5])
                        print(f"PORT set: host={data_host}, port={data_port}")
                        send_response(client_sock, 200, "PORT command successful")
                    except Exception as e:
                        print(f"PORT failed: {str(e)}")
                        send_response(client_sock, 501, f"PORT failed: {str(e)}")
                        data_host, data_port = client_addr[0], DATA_PORT 
                
                case _ if not authenticated:
                    send_response(client_sock, 530, "Not logged in")
                
                case 'LIST' | 'NLST' | 'DIR':
                    try:
                        print(f"Attempting data connection to {data_host}:{data_port}")
                        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        data_sock.settimeout(5)
                        data_sock.connect((data_host, data_port))
                        send_response(client_sock, 150, "Opening data connection")
                        files = os.listdir(current_dir)
                        print(f"Files in {current_dir}: {files}")
                        listing = '\r\n'.join(files)
                        data_sock.send(listing.encode())
                        data_sock.close()
                        send_response(client_sock, 226, "Transfer complete")
                    except socket.timeout:
                        send_response(client_sock, 550, "Data connection timed out")
                    except Exception as e:
                        send_response(client_sock, 550, f"Failed: {str(e)}")
                
                case 'RETR':
                    file_path = os.path.join(current_dir, args)
                    if os.path.isfile(file_path):
                        try:
                            print(f"Attempting data connection to {data_host}:{data_port}")
                            data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            data_sock.settimeout(5)
                            data_sock.connect((data_host, data_port))
                            send_response(client_sock, 150, "Opening data connection")
                            with open(file_path, 'rb') as f:
                                while True:
                                    chunk = f.read(1024)
                                    if not chunk:
                                        break
                                    data_sock.send(chunk)
                            data_sock.close()
                            send_response(client_sock, 226, "Transfer complete")
                        except socket.timeout:
                            send_response(client_sock, 550, "Data connection timed out")
                        except Exception as e:
                            send_response(client_sock, 550, f"Failed: {str(e)}")
                    else:
                        send_response(client_sock, 550, "File not found")
                
                case 'STOR':
                    file_path = os.path.join(current_dir, args)
                    try:
                        print(f"Attempting data connection to {data_host}:{data_port}")
                        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        data_sock.settimeout(5)
                        data_sock.connect((data_host, data_port))
                        send_response(client_sock, 150, "Opening data connection")
                        with open(file_path, 'wb') as f:
                            while True:
                                chunk = data_sock.recv(1024)
                                if not chunk:
                                    break
                                f.write(chunk)
                        data_sock.close()
                        send_response(client_sock, 226, "Transfer complete")
                    except socket.timeout:
                        send_response(client_sock, 550, "Data connection timed out")
                    except Exception as e:
                        send_response(client_sock, 550, f"Failed: {str(e)}")
                
                case _:
                    send_response(client_sock, 502, f"Command not implemented: {command}")

        except Exception as e:
            send_response(client_sock, 500, f"Error: {str(e)}")
            break

    client_sock.close()

def main():
    if not initialize_ftp_root():
        print("Failed to initialize FTP root directory. Exiting.")
        sys.exit(1)

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(5)
    print(f"FTP server running on {HOST}:{PORT}")

    while True:
        try:
            client_sock, client_addr = server_sock.accept()
            print(f"New connection from {client_addr}")
            handle_client(client_sock, client_addr)
        except KeyboardInterrupt:
            print("\nShutting down server")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

    server_sock.close()

if __name__ == '__main__':
    main()