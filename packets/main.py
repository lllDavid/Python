import struct

class Packet:
    """
    Packet format:
    - 2 bytes: packet type (unsigned short)
    - 4 bytes: payload length (unsigned int)
    - payload: variable length bytes
    """

    HEADER_FORMAT = "!HI"  
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

    def __init__(self, packet_type, payload):
        self.packet_type = packet_type
        self.payload = payload  
    def encode(self):
        payload_length = len(self.payload)
        header = struct.pack(self.HEADER_FORMAT, self.packet_type, payload_length)
        return header + self.payload

    @classmethod
    def decode(cls, packet_bytes):
        header = packet_bytes[:cls.HEADER_SIZE]
        packet_type, payload_length = struct.unpack(cls.HEADER_FORMAT, header)
        payload = packet_bytes[cls.HEADER_SIZE:cls.HEADER_SIZE + payload_length]
        return cls(packet_type, payload)

    def __repr__(self):
        return f"<Packet type={self.packet_type} payload={self.payload}>"
    
if __name__ == "__main__":
    packet = Packet(1, b"Hello, world!")
    encoded = packet.encode()
    print(f"Encoded bytes: {encoded}")

    decoded_packet = Packet.decode(encoded)
    print(f"Decoded packet: {decoded_packet}")
    print(f"Payload as string: {decoded_packet.payload.decode()}")
