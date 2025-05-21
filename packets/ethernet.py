import struct

def mac_str_to_bytes(mac_str):
    return bytes(int(b, 16) for b in mac_str.split(':'))

def build_ethernet_frame(dst_mac, src_mac, ethertype, payload):
    dst_mac_bytes = mac_str_to_bytes(dst_mac)
    src_mac_bytes = mac_str_to_bytes(src_mac)
    ethertype_bytes = struct.pack('!H', ethertype)

    frame = dst_mac_bytes + src_mac_bytes + ethertype_bytes + payload
    return frame

if __name__ == "__main__":
    dst_mac = "ff:ff:ff:ff:ff:ff" 
    src_mac = "00:11:22:33:44:55"  
    ethertype = 0x0800  

    payload = b"Ethernet Payload!"

    ethernet_frame = build_ethernet_frame(dst_mac, src_mac, ethertype, payload)
    print(f"Ethernet frame bytes: {ethernet_frame.hex()}")
