import socket

addr = ""
port = ""

b_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
b_socket.connect(addr,port)
