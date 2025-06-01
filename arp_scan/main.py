#!/usr/bin/env python3

import subprocess
import ipaddress
import threading

def ping(ip):
    subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_arp_table():
    result = subprocess.run(['ip', 'neigh'], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

def arp_scan(network):
    print(f"Scanning network: {network}\n")

    threads = []
    for ip in ipaddress.IPv4Network(network, strict=False):
        t = threading.Thread(target=ping, args=(ip,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("IP Address\tMAC Address")
    print("-" * 40)
    for entry in get_arp_table():
        parts = entry.split()
        if 'lladdr' in parts:
            ip = parts[0]
            mac = parts[4]
            print(f"{ip}\t{mac}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: sudo python3 main.py <CIDR>")
        sys.exit(1)

    arp_scan(sys.argv[1])
