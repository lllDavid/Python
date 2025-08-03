import socket
import struct
import os

def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    return ~s & 0xffff

def create_icmp_packet(id, seq, payload=b'Hello'):
    header = struct.pack('!BBHHH', 8, 0, 0, id, seq)
    data = payload
    chksum = checksum(header + data)
    header = struct.pack('!BBHHH', 8, 0, chksum, id, seq)
    return header + data

def send_icmp_echo(host):
    id = os.getpid() & 0xFFFF
    seq = 1
    packet = create_icmp_packet(id, seq)
    for _ in  range(10):
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
            sock.settimeout(2)
            sock.sendto(packet, (host, 0))

            try:
                recv_packet, addr = sock.recvfrom(1024)
                print(f"Received reply from {addr[0]}")
            except socket.timeout:
                print("Request timed out")

if __name__ == "__main__":
    send_icmp_echo("")