import socket
import struct

def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
        while True:
            packet, addr = sock.recvfrom(65535)
            ip_header = packet[:20]
            icmp_header = packet[20:28]
            data = packet[28:]
            
            icmp_type, code, chksum, ident, seq = struct.unpack('!BBHHH', icmp_header)
            
            if icmp_type == 8:  
                try:
                    msg = data.decode(errors='ignore')
                    print(f"[{addr[0]}] ICMP payload: {msg}")
                except UnicodeDecodeError:
                    continue

if __name__ == "__main__":
    receive()