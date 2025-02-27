import socket
import struct
import os
from ipaddress import ip_network

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def create_arp_request(sender_ip, target_ip):
    hardware_type = 1
    protocol_type = 0x0800
    hardware_size = 6
    protocol_size = 4
    op_code = 1
    sender_mac = os.urandom(6)
    sender_ip = socket.inet_aton(sender_ip)
    target_ip = socket.inet_aton(target_ip)
    arp_request = struct.pack(
        "!HHBBH6s4s6s4s", 
        hardware_type, protocol_type, hardware_size, protocol_size,
        op_code, sender_mac, sender_ip, b'\x00\x00\x00\x00\x00\x00', target_ip
    )
    return arp_request

def send_arp_request(target_ip):
    local_ip = get_local_ip()
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    dest_mac = b'\xff\xff\xff\xff\xff\xff'
    src_mac = os.urandom(6)
    eth_header = struct.pack("!6s6sH", dest_mac, src_mac, 0x0806)
    arp_request = create_arp_request(local_ip, target_ip)
    raw_socket.send(eth_header + arp_request)
    print(f"[*] ARP Request sent for {target_ip} from {local_ip}")
    raw_socket.close()

def arp_scan(network):
    for ip in ip_network(network, strict=False).hosts():
        send_arp_request(str(ip))

if __name__ == "__main__":
    network = "192.168.1.0/24"
    arp_scan(network)
