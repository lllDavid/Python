import socket
import struct
import binascii

def create_raw_socket():
    try:
        raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        return raw_socket
    except Exception as e:
        print(f"Error creating raw socket: {e}")
        exit(1)

def build_arp_request(target_ip, source_ip, interface):
    destination_mac = b'\xff\xff\xff\xff\xff\xff'
    source_mac = get_mac_address(interface)
    eth_header = struct.pack('!6s6sH', destination_mac, source_mac, 0x0806)
    arp_header = struct.pack('!HHBBH6s4s6s4s',
                             1,
                             0x0800,
                             6,
                             4,
                             1,
                             source_mac,
                             socket.inet_aton(source_ip),
                             b'\x00\x00\x00\x00\x00\x00',
                             socket.inet_aton(target_ip)
                             )
    return eth_header + arp_header

def get_mac_address(interface):
    with open(f'/sys/class/net/{interface}/address', 'r') as f:
        return binascii.unhexlify(f.read().replace(":", "")).decode("utf-8")

def arp_scan(target_ip, source_ip, interface='eth0'):
    raw_socket = create_raw_socket()
    arp_request_packet = build_arp_request(target_ip, source_ip, interface)
    raw_socket.sendto(arp_request_packet, (interface, 0))
    
    while True:
        packet = raw_socket.recv(65535)
        eth_header = packet[:14]
        eth_fields = struct.unpack('!6s6sH', eth_header)
        ethertype = eth_fields[2]
        
        if ethertype == 0x0806:
            arp_header = packet[14:42]
            arp_fields = struct.unpack('!HHBBH6s4s6s4s', arp_header)
            opcode = arp_fields[4]
            
            if opcode == 2:
                target_mac = binascii.hexlify(arp_fields[5]).decode('utf-8')
                target_ip = socket.inet_ntoa(arp_fields[7])
                print(f"IP Address: {target_ip}\tMAC Address: {target_mac}")
                break

target_ip = "192.168.1.1"
source_ip = "192.168.1.100"

arp_scan(target_ip, source_ip)
