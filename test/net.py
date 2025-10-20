#!/usr/bin/env python3
import socket
import selectors
import threading
import time

HOST = "127.0.0.1"
PORT = 5001
sel = selectors.DefaultSelector()

def handle_client(conn, addr):
    print(f"Server: Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"Server: Connection closed by {addr}")
                break
            print(f"Server received: {data.decode().strip()}")
            conn.sendall(data)  
        except ConnectionResetError:
            break
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = server_sock.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

def read(sock):
    try:
        data = sock.recv(1024)
        if data:
            print("Client received:", data.decode().strip())
        else:
            sel.unregister(sock)
            sock.close()
    except BlockingIOError:
        pass

def start_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        sock.connect_ex((HOST, PORT))
    except BlockingIOError:
        pass
    sel.register(sock, selectors.EVENT_READ, read)
    sock.sendall(b"Hello from async client\n")

    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    
    time.sleep(0.5)
    
    start_client()