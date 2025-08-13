import socket
import struct

def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i+1] if i+1 < len(msg) else 0)
        s += w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

src_ip = '192.168.1.100'
dst_ip = '192.168.1.1'
src_port = 1234
dst_port = 53
payload = b'Payload here'

ip_ver = 4
ip_ihl = 5
ip_tos = 0
ip_tot_len = 20 + 8 + len(payload)
ip_id = 54321
ip_frag_off = 0
ip_ttl = 64
ip_proto = socket.IPPROTO_UDP
ip_check = 0
ip_saddr = socket.inet_aton(src_ip)
ip_daddr = socket.inet_aton(dst_ip)

ip_ihl_ver = (ip_ver << 4) + ip_ihl
ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len,
                        ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check,
                        ip_saddr, ip_daddr)

udp_len = 8 + len(payload)
udp_check = 0
udp_header = struct.pack('!HHHH', src_port, dst_port, udp_len, udp_check)

pseudo_header = ip_saddr + ip_daddr + struct.pack('!BBH', 0, ip_proto, udp_len)
udp_check_data = pseudo_header + udp_header + payload
udp_check = checksum(udp_check_data)

udp_header = struct.pack('!HHHH', src_port, dst_port, udp_len, udp_check)

packet = ip_header + udp_header + payload

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
sock.sendto(packet, (dst_ip, 0))