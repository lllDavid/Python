import struct
import socket

def checksum(data):
    if len(data) % 2:
        data += b'\x00'
    s = sum(struct.unpack("!%dH" % (len(data)//2), data))
    s = (s >> 16) + (s & 0xffff)
    s += s >> 16
    return ~s & 0xffff

def build_ipv4_packet(src_ip, dst_ip, payload, protocol=6, identification=54321, ttl=64):
    version = 4
    ihl = 5  
    ver_ihl = (version << 4) + ihl
    tos = 0
    total_length = 20 + len(payload)  
    flags = 2
    fragment_offset = 0
    flags_fragment = (flags << 13) + fragment_offset
    header_checksum = 0  

    src_ip_bytes = socket.inet_aton(src_ip)
    dst_ip_bytes = socket.inet_aton(dst_ip)

    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ver_ihl,
        tos,
        total_length,
        identification,
        flags_fragment,
        ttl,
        protocol,
        header_checksum,
        src_ip_bytes,
        dst_ip_bytes
    )

    header_checksum = checksum(ip_header)

    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ver_ihl,
        tos,
        total_length,
        identification,
        flags_fragment,
        ttl,
        protocol,
        header_checksum,
        src_ip_bytes,
        dst_ip_bytes
    )

    return ip_header + payload

if __name__ == "__main__":
    src_ip = "192.168.1.1"
    dst_ip = "192.168.1.2"
    payload = b"IPV4 Payload"
    protocol = 6  

    ip_packet = build_ipv4_packet(src_ip, dst_ip, payload, protocol)
    print(f"IPv4 packet bytes: {ip_packet.hex()}")