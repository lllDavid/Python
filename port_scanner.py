import socket

def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        try:
            print(f"Scanning {target}:{port}...") 
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning {target}:{port} - {e}")  
            sock.close()

    return open_ports

if __name__ == "__main__":
    target_host = ""
    start_port = 1
    end_port = 100

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_host}")