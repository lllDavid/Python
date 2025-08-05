import socket
import struct
import os

def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += (data[i] << 8) + data[i + 1]
    if n:
        s += data[-1] << 8
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    return ~s & 0xFFFF

def create_icmp_packet(id, seq):
    type = 8      
    code = 0
    chksum = 0
    header = struct.pack('!BBHHH', type, code, chksum, id, seq)
    payload = b'PINGTESTDATA'
    chksum = checksum(header + payload)
    header = struct.pack('!BBHHH', type, code, chksum, id, seq)
    return header + payload

def send_icmp_packet(dest_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet_id = os.getpid() & 0xFFFF
    seq = 1
    packet = create_icmp_packet(packet_id, seq)
    sock.sendto(packet, (dest_ip, 0))
    print(f"Sent ICMP Echo Request to {dest_ip}")

if __name__ == "__main__":
    send_icmp_packet("8.8.8.8") 