import struct

def build_tcp_packet(
    src_port, dst_port, seq_num, ack_num,
    data_offset=5,  
    flags=0x02,    
    window=8192,
    urgent_ptr=0,
    payload=b""
):
    offset_reserved_flags = (data_offset << 12) + flags  

    tcp_header = struct.pack(
        '!HHLLHHHH',
        src_port,           
        dst_port,           
        seq_num,            
        ack_num,            
        offset_reserved_flags,
        window,
        0,                  
        urgent_ptr
    )

    return tcp_header + payload


if __name__ == "__main__":
    src_port = 12345
    dst_port = 80
    seq_num = 0
    ack_num = 0
    flags = 0x02 
    payload = b""

    tcp_packet = build_tcp_packet(src_port, dst_port, seq_num, ack_num, flags=flags, payload=payload)
    print(f"Raw TCP packet bytes: {tcp_packet.hex()}")
