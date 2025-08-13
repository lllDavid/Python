import struct

def mac_str_to_bytes(mac):
    return bytes.fromhex(mac.replace(":", ""))

def create_ethernet_frame(dst_mac, src_mac, eth_type, payload):
    dst_mac_bytes = mac_str_to_bytes(dst_mac)
    src_mac_bytes = mac_str_to_bytes(src_mac)
    eth_type_bytes = struct.pack("!H", eth_type)  

    frame = dst_mac_bytes + src_mac_bytes + eth_type_bytes + payload

    return frame

dst_mac = "AA:BB:CC:DD:EE:FF"
src_mac = "11:22:33:44:55:66"
eth_type = 0x0800 
payload = b"Test Payload" + b"\x00" * (46 - len("Test Payload"))  

frame = create_ethernet_frame(dst_mac, src_mac, eth_type, payload)

print("Ethernet Frame (hex):", frame.hex())