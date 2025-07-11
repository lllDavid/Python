import socket
import struct

def query(domain):
    server = ("8.8.8.8", 53)
    query = b'\xaa\xaa'          
    query += b'\x01\x00'         
    query += b'\x00\x01\x00\x00\x00\x00\x00\x00'
    for part in domain.split('.'):
        query += bytes([len(part)]) + part.encode()
    query += b'\x00\x00\x01\x00\x01'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(query, server)
    data, _ = s.recvfrom(512)
    s.close()
    return data

def parses_response(data):
    qdcount = struct.unpack(">H", data[4:6])[0]

    idx = 12
    for _ in range(qdcount):
        while data[idx] != 0:
            idx += data[idx] + 1
        idx += 1  
        idx += 4  

    idx += 2  
    rtype = struct.unpack(">H", data[idx:idx+2])[0]
    idx += 2
    rclass = struct.unpack(">H", data[idx:idx+2])[0]
    idx += 2
    ttl = struct.unpack(">I", data[idx:idx+4])[0]
    idx += 4
    rdlength = struct.unpack(">H", data[idx:idx+2])[0]
    idx += 2

    rdata = data[idx:idx+rdlength]

    if rtype == 1 and rclass == 1 and rdlength == 4:
        ip = ".".join(str(b) for b in rdata)
        return ip
    return None

response = query("")
ip = parses_response(response)
print("IP address:", ip)