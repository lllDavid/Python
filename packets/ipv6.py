import struct
import socket

def build_ipv6_packet(src_ip, dst_ip, payload, next_header=6, hop_limit=64):
    version = 6
    traffic_class = 0
    flow_label = 0

    version_traffic_flow = (version << 28) | (traffic_class << 20) | flow_label

    payload_length = len(payload)

    src_ip_bytes = socket.inet_pton(socket.AF_INET6, src_ip)
    dst_ip_bytes = socket.inet_pton(socket.AF_INET6, dst_ip)

    ipv6_header = struct.pack(
        "!IHBB16s16s",
        version_traffic_flow,
        payload_length,
        next_header,
        hop_limit,
        src_ip_bytes,
        dst_ip_bytes
    )

    return ipv6_header + payload

if __name__ == "__main__":
    src_ip = "2001:0db8:85a3::8a2e:0370:7334"
    dst_ip = "2001:0db8:85a3::8a2e:0370:7335"
    payload = b"IPV6 Payload"
    next_header = 6  

    ipv6_packet = build_ipv6_packet(src_ip, dst_ip, payload, next_header)
    print(f"IPv6 packet bytes: {ipv6_packet.hex()}")
