import socket
import threading

def handle_client(client_socket, client_address):
    try:
        print(f"New connection from {client_address}")
        client_socket.send("Welcome to the server!".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                print(f"Connection closed by {client_address}")
                break
            print(f"Received from {client_address}: {message}")
            client_socket.send(f"Echo: {message}".encode('utf-8'))

    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except Exception as e:
        print(f"Error starting the server: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()