import socket
import psutil
import platform
import subprocess
from datetime import datetime

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def get_local_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
        except OSError:
            return 'Unavailable'

def get_hostname_info():
    print("Host Information")
    try:
        hostname = socket.gethostname()
        local_ip = get_local_ip()
    except OSError:
        hostname = "Unavailable"
        local_ip = "Unavailable"
    print(f"Hostname      : {hostname}")
    print(f"Local IP      : {local_ip}\n")

def get_interface_info():
    print("Network Interfaces")
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for iface, addrs in interfaces.items():
        print(f"Interface: {iface}")
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"  IPv4 Address : {addr.address}")
                print(f"  Netmask      : {addr.netmask}")
            elif addr.family == socket.AF_INET6:
                print(f"  IPv6 Address : {addr.address}")
                print(f"  Netmask      : {addr.netmask}")
        stat = stats.get(iface)
        if stat:
            print(f"  Is Up        : {stat.isup}")
            print(f"  Speed        : {stat.speed} Mbps")
        print()

def get_default_gateway():
    print("Default Gateway")
    system = platform.system().lower()

    if system == "windows":
        output = subprocess.check_output("ipconfig", shell=True, text=True)
        for line in output.splitlines():
            if "Default Gateway" in line:
                gateway_ip = line.split(":")[-1].strip()
                if gateway_ip:
                    print(line.strip())
    elif system == "linux":
        output = run_command("ip route show default")
        if output:
            print(output)
        else:
            print("Could not retrieve default gateway.")
    elif system == "darwin":
        output = run_command("ip route get 8.8.8.8")
        if output:
            print(output)
        else:
            print("Could not retrieve default gateway.")
    else:
        print("Unsupported OS for default gateway detection.")
    print()

def get_arp_table():
    print("ARP Cache")
    system = platform.system().lower()
    if system == "windows":
        cmd = "arp -a"
    elif system == "linux":
        cmd = "ip neigh show"
    else:
        cmd = "arp -n"
    output = run_command(cmd)
    if output:
        print(output)
    else:
        print("Failed to get ARP cache.")
    print()

def get_routing_table():
    print("Routing Table")
    system = platform.system().lower()
    if system == "windows":
        cmd = "route print"
    elif system == "linux":
        cmd = "ip route show"
    else:
        cmd = "netstat -rn"
    output = run_command(cmd)
    if output:
        print(output)
    else:
        print("Failed to get routing table.")
    print()

def main():
    print("Local Network Diagnostic Report")
    print(f"Generated: {datetime.now()}\n")

    get_hostname_info()
    get_default_gateway()
    get_interface_info()
    get_arp_table()
    get_routing_table()

if __name__ == "__main__":
    main()