import socket

addr = ""
port = ""

def connect():
    b_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    b_socket.bind(addr,port)
    b_socket.listen(1)
    print("Ready to receive data")
    while True:
        conn, addr = b_socket.accept()

connect()


