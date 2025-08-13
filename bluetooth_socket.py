import socket

host = ""  
port = 5   

def start_server(host, port):
    b_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    b_socket.bind((host, port))
    b_socket.listen(1)
    print("Ready to receive data...")
    
    while True:
        try:
            conn, addr = b_socket.accept()
            print(f"Connected to {addr}")

        except Exception as e:
            print(f"An error occurred: {e}")

start_server(host, port)