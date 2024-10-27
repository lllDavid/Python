import socket

host = "SERVER_BLUETOOTH_ADDRESS"  
port = 5

def connect_to_server(host, port):
    client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        client_socket.send(b"Message from client.")
        print("Data sent to server.")
        
        client_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")

connect_to_server(host, port)
