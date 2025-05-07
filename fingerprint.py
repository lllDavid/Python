from dataclasses import dataclass, field
from subprocess import run
from ctypes import windll
from uuid import getnode
import os

@dataclass
class Fingerprint:
    username_history: set[str] = field(default_factory=set)
    email_address_history: set[str] = field(default_factory=set)
    mac_address: str | None = None
    associated_ips: dict[str, int] | None = None
    device_id: str | None = None
    device_type: str | None = None
    device_manufacturer: str | None = None
    device_model: str | None = None
    screen_resolution: tuple | None = None
    geolocation_country: str | None = None
    geolocation_city: str | None = None
    geolocation_latitude: float | None = None
    geolocation_longitude: float | None = None
    avg_login_frequency: dict[str, float] | None = None
    avg_session_duration: dict[str, float] | None = None
    behavioral_biometrics: dict[str, float] | None = None
    browser_info: str | None = None
    os_name: str | None = None
    os_version: str | None = None
    vpn_usage: bool | None = None
    user_preferences: dict[str, str] | None = None
    user_agent: str | None = None
    two_factor_enabled: bool | None = None


    def create_fingerprint(self):
        # MAC Address
        self.mac_address = ':'.join(['{:02x}'.format((getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
        # Device ID
        match(os.name):

            case("nt"):  
                self.device_id = run(['wmic', 'csproduct', 'get', 'uuid'], capture_output=True, text=True).stdout.strip().split('\n')[2].strip()

            case("posix"):
                with open("/sys/class/dmi/id/product_uuid", "r") as f:
                    self.device_id = f.read().strip()
        # Screen Resolution
        user32 = windll.user32
        user32.SetProcessDPIAware()
        width = user32.GetSystemMetrics(0)
        height = user32.GetSystemMetrics(1)
        self.screen_resolution = (width, height)



f = Fingerprint()

f.create_fingerprint()

print("MAC:", f.mac_address)
print("Device-ID:", f.device_id)
print("Screen Resolution:", f.screen_resolution)