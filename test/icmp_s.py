import socket
import struct
import sys

def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    res = sum(struct.unpack("!%dH" % (len(data) // 2), data))
    res = (res >> 16) + (res & 0xffff)
    res += res >> 16
    return ~res & 0xffff

def send(host, payload, id=1234, seq=1):
    header = struct.pack('!BBHHH', 8, 0, 0, id, seq)
    data = payload.encode()
    chksum = checksum(header + data)
    header = struct.pack('!BBHHH', 8, 0, chksum, id, seq)
    packet = header + data

    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as sock:
        sock.sendto(packet, (host, 0))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: sudo python {sys.argv[0]} <target_ip> <message>")
        sys.exit(1)
    send(sys.argv[1], sys.argv[2])