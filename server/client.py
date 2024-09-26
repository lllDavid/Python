import socket

def client():
    host = 'localhost'  
    port = 8229       

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        command = input("Enter command (register/login) or 'exit' to quit: ")
        if command == 'exit':
            break

        client_socket.sendall(command.encode())

        if command == "register":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            client_socket.sendall(username.encode())
            client_socket.sendall(password.encode())
            client_socket.sendall(email.encode())
      
        elif command == "login":
            username = input("Enter username: ")
            password = input("Enter password: ")
            client_socket.sendall(username.encode())
            client_socket.sendall(password.encode())
       
        else:
            print("Unknown command.")

    client_socket.close()

client()
