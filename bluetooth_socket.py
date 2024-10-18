import socket

host = ""
port = "5"

def connect(host,port):
    b_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    b_socket.bind(host,port)
    b_socket.listen(1)
    print("Ready to receive data")
    while True:
        conn, addr = b_socket.accept()
        print(f"Connected devices {conn}")
        

connect(host,port)


