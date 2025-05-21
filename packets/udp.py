import struct

def build_udp_packet(src_port, dst_port, payload):
    length = 8 + len(payload)  
    checksum = 0  

    udp_header = struct.pack('!HHHH', src_port, dst_port, length, checksum)
    return udp_header + payload

if __name__ == "__main__":
    src_port = 12345
    dst_port = 80
    payload = b"Test Payload"

    udp_packet = build_udp_packet(src_port, dst_port, payload)
    print(f"Raw UDP packet bytes: {udp_packet.hex()}")
