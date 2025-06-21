import socket

class Manager:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sock:
            self.sock.close()

with Manager('example.com', 80) as s:
    s.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = s.recv(4096)
    print(response)