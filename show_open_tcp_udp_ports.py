import psutil
import socket

connectall = psutil.net_connections(kind='inet')
only_udp = [conn for conn in psutil.net_connections(kind='inet') if conn.type == socket.SOCK_DGRAM]

only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN]

only_udp_listening_ports = [conn.laddr.port for conn in only_udp]

only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

for port in only_tcp_listening_ports:
    print(f"TCP port = {port} Open")

print("\n")

for port in only_udp_listening_ports:
    print(f"UDP port = {port} Open")