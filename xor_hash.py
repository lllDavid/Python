def hash(data):
    hash_value = 0x345678 
    prime1 = 37
    prime2 = 101

    for i, char in enumerate(data):
        ascii_value = ord(char)
        hash_value ^= (ascii_value * prime1)
        hash_value += (ascii_value << (i % 5)) 
        hash_value = (hash_value * prime2) % (2**32)  

        hash_value = ((hash_value << 7) | (hash_value >> 25)) & 0xFFFFFFFF

    return hash_value