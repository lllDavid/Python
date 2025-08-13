import socket

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port)) 
    print(f"Server started on {host}:{port}. Waiting for streaming data...")

    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)  
            if not data:
                print("No data received. Connection might be closed.")
                break

            received_data = data.decode('utf-8')
            print(f"Received streaming data from {client_address}: {received_data}")

            response = f"Data received: {received_data}"
            server_socket.sendto(response.encode('utf-8'), client_address)

        except KeyboardInterrupt:
            print("Server interrupted, closing...")
            break
        except Exception as e:
            print(f"Error: {e}")

    server_socket.close()

if __name__ == "__main__":
    start_server()