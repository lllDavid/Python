import subprocess
import re

WHITELIST = {"00-11-22-33-44-55", "66-77-88-99-AA-BB", ...}

def get_connected():
    try:    
        result = subprocess.check_output("arp -a", shell=True).decode() # Win: arp -a, Linux: arp -n 
    except subprocess.CalledProcessError:
        return []

    macs = []
    for line in result.splitlines():
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([-\w]+)\s+(\w+)", line)
        if match:
            ip = match.group(1)
            mac = match.group(2).upper()
            if mac != "FF-FF-FF-FF-FF-FF" and mac != "00-00-00-00-00-00":
                macs.append((ip, mac))
    return macs

def check_whitelist():
    for ip, mac in get_connected():
        if mac not in WHITELIST:
            print(f"Device {ip} with MAC {mac} is not whitelisted.")

check_whitelist()