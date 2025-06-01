import socket
import struct
import random

def checksum(data):
    if not isinstance(data, bytes):
        raise TypeError("Data must be bytes")
    s = 0
    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i+1] if (i+1) < len(data) else 0)
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = s + (s >> 16)
    return ~s & 0xffff

def create_ip_header(src_ip, dst_ip, tcp_header_len):
    ip_ihl = 5
    ip_ver = 4
    ip_tos = 0
    ip_tot_len = 20 + tcp_header_len  
    ip_id = 54321
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = socket.IPPROTO_TCP
    ip_check = 0
    try:
        ip_saddr = socket.inet_aton(src_ip)
        ip_daddr = socket.inet_aton(dst_ip)
    except OSError:
        raise ValueError("Invalid IP address format")

    ip_ihl_ver = (ip_ver << 4) + ip_ihl

    ip_header = struct.pack('!BBHHHBBH4s4s',
                            ip_ihl_ver, ip_tos, ip_tot_len, ip_id,
                            ip_frag_off, ip_ttl, ip_proto, ip_check,
                            ip_saddr, ip_daddr)

    ip_check = checksum(ip_header)
    ip_header = struct.pack('!BBHHHBBH4s4s',
                            ip_ihl_ver, ip_tos, ip_tot_len, ip_id,
                            ip_frag_off, ip_ttl, ip_proto, ip_check,
                            ip_saddr, ip_daddr)
    return ip_header

def create_tcp_header(src_ip, dst_ip, src_port, dst_port):
    tcp_source = src_port
    tcp_dest = dst_port
    tcp_seq = random.randint(0, 0xFFFFFFFF)
    tcp_ack_seq = 0
    tcp_doff = 5
    tcp_flags = 2  
    tcp_window = socket.htons(5840)
    tcp_check = 0
    tcp_urg_ptr = 0

    tcp_offset_res = (tcp_doff << 4) + 0

    tcp_header = struct.pack('!HHLLBBHHH',
                             tcp_source, tcp_dest, tcp_seq, tcp_ack_seq,
                             tcp_offset_res, tcp_flags, tcp_window,
                             tcp_check, tcp_urg_ptr)

    try:
        source_address = socket.inet_aton(src_ip)
        dest_address = socket.inet_aton(dst_ip)
    except OSError:
        raise ValueError("Invalid IP address format")

    psh = struct.pack('!4s4sBBH',
                      source_address, dest_address, 0,
                      socket.IPPROTO_TCP, len(tcp_header))
    psh = psh + tcp_header

    tcp_check = checksum(psh)

    tcp_header = struct.pack('!HHLLBBHHH',
                             tcp_source, tcp_dest, tcp_seq, tcp_ack_seq,
                             tcp_offset_res, tcp_flags, tcp_window,
                             tcp_check, tcp_urg_ptr)
    return tcp_header

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except PermissionError:
        print("Run this script as admin!")
        return

    src_ip = '192.168.1.100'  
    dst_ip = '192.168.1.1'    
    src_port = 1234
    dst_port = 80

    tcp_header = create_tcp_header(src_ip, dst_ip, src_port, dst_port)
    ip_header = create_ip_header(src_ip, dst_ip, len(tcp_header))

    packet = ip_header + tcp_header

    try:
        s.sendto(packet, (dst_ip, 0))
        print("Packet sent!")
    except OSError as e:
        print(f"Failed to send packet: {e}")

if __name__ == '__main__':
    main()