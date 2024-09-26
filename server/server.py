import json
import socket

class Server:
    def __init__(self):
        self.users = []
        self.load_users()

    def start_server(self, host='localhost', port=8229):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")
            self.handle_client(conn)
        
        server_socket.close()

    def handle_client(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")

            if message == "register":
                self.register_user(conn)
            elif message == "login":
                self.login_user(conn)
            else:
                conn.sendall("Unknown command".encode())

        conn.close()

    def load_users(self):
        try:
            with open("user_data.json", 'r', encoding='utf-8') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []

    def register_user(self, conn):
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()
        email = conn.recv(1024).decode()
        
        userdata = {
            "username": username,
            "password": password,
            "email": email
        }
        self.users.append(userdata)
        self.save_users()
        conn.sendall("Registration successful!".encode())
        print(f"Registered user: {userdata}")

    def save_users(self):
        with open("user_data.json", 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=4)
        print("Data saved.")

    def login_user(self, conn):
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()

        for user in self.users:
            if user['username'] == username and user['password'] == password:
                conn.sendall(f"Hi {username}!".encode())
                return

        conn.sendall("Wrong credentials.".encode())

if __name__ == "__main__":
    server = Server()
    server.start_server()


        