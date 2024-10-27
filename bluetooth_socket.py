import socket

host = ""  # Bind to all available interfaces
port = 5   # Port must be an integer

def connect(host, port):
    # Create a Bluetooth socket
    b_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    
    # Bind the socket to the host and port
    b_socket.bind((host, port))
    b_socket.listen(1)
    print("Ready to receive data...")
    
    while True:
        try:
            # Wait for a connection
            conn, addr = b_socket.accept()
            print(f"Connected to {addr}")

            # You can add further code here to handle the connection
            # e.g., receive data from the connected device

        except Exception as e:
            print(f"An error occurred: {e}")

# Start the connection
connect(host, port)
