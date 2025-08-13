from dataclasses import dataclass
from subprocess import run
from uuid import getnode
import re
import os

@dataclass
class LocalData:
    mac_address: str | None = None
    device_id: str | None = None
    screen_resolution: tuple | None = None

    def collect_info(self):
        # MAC Address
        self.mac_address = ':'.join(
            ['{:02x}'.format((getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]
        )
        match os.name:
            case "nt":  # Windows Device ID
                self.device_id = run(
                    ['wmic', 'csproduct', 'get', 'uuid'], capture_output=True, text=True
                ).stdout.strip().split('\n')[2].strip()
                # Windows Screen Resolution
                from ctypes import windll  
                user32 = windll.user32
                user32.SetProcessDPIAware()
                width = user32.GetSystemMetrics(0)
                height = user32.GetSystemMetrics(1)
                self.screen_resolution = (width, height)
            case "posix":  # Unix Device ID
                    with open("/sys/class/dmi/id/product_uuid", "r") as f:
                        self.device_id = f.read().strip()
                 # Unix Screen Resolution
                    output = run(["xrandr"], capture_output=True, text=True).stdout
                    match = re.search(r'current\s+(\d+)\s+x\s+(\d+)', output)
                    if match:
                        width, height = int(match.group(1)), int(match.group(2))
                        self.screen_resolution = (width, height)             

ld = LocalData()
ld.collect_info()

print("MAC:", ld.mac_address)
print("Device-ID:", ld.device_id)
print("Screen Resolution:", ld.screen_resolution)