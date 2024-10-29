import psutil

def list_open_ports():
    open_ports = []
    for conn in psutil.net_connections(kind='inet'):
        open_ports.append((conn.laddr.ip, conn.laddr.port, conn.raddr, conn.status))
    return open_ports

if __name__ == "__main__":
    ports = list_open_ports()
    for ip, port, raddr, status in ports:
        print(f"IP: {ip}, Port: {port}, Remote Address: {raddr}, Status: {status}")
import psutil

def list_open_ports():
    open_ports = []
    for conn in psutil.net_connections(kind='inet'):
        open_ports.append((conn.laddr.ip, conn.laddr.port, conn.raddr, conn.status))
    return open_ports

if __name__ == "__main__":
    ports = list_open_ports()
    for ip, port, raddr, status in ports:
        print(f"Port: {port}, Remote Address: {raddr}, Status: {status}")
