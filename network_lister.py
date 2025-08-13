import subprocess

def list_wifi_networks():
    encodings_to_try = ["utf-8", "latin-1", "cp1252", "iso-8859-1"]

    for encoding in encodings_to_try:
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=Bssid"])
            decoded_result = result.decode(encoding)
            print(decoded_result)
            break 
        except (subprocess.CalledProcessError, UnicodeDecodeError) as e:
            print(f"Error with encoding {encoding}: {e}")

if __name__ == "__main__":
    list_wifi_networks()