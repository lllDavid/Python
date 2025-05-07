from dataclasses import dataclass, field
from subprocess import run
from ctypes import windll
from uuid import getnode
import os

@dataclass
class LocalData:
    mac_address: str | None = None
    device_id: str | None = None
    screen_resolution: tuple | None = None

    def collect_info(self):
        # MAC Address
        self.mac_address = ':'.join(['{:02x}'.format((getnode() >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1])
        # Device ID
        match os.name:
            case "nt":  
                self.device_id = run(['wmic', 'csproduct', 'get', 'uuid'], capture_output=True, text=True).stdout.strip().split('\n')[2].strip()
            case "posix":
                with open("/sys/class/dmi/id/product_uuid", "r") as f:
                    self.device_id = f.read().strip()
        # Screen Resolution
        user32 = windll.user32
        user32.SetProcessDPIAware()
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        self.screen_resolution = (width, height)

ld = LocalData()
ld.collect_info()

print("MAC:", ld.mac_address)
print("Device-ID:", ld.device_id)
print("Screen Resolution:", ld.screen_resolution)