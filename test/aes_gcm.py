from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt(plaintext: bytes):
    key = os.urandom(32)   
    nonce = os.urandom(12) 
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    tag = encryptor.tag  
    return key, nonce, ciphertext, tag

def decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes):
    decryptor = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend()).decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

if __name__ == "__main__":
    user_input = input("Enter: ").encode()
    key, nonce, ciphertext, tag = encrypt(user_input)

    print("\nEncrypted data:")
    print("Key:", key.hex())
    print("Nonce:", nonce.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Tag:", tag.hex())

    decrypted = decrypt(key, nonce, ciphertext, tag)
    print("\nDecrypted data:")
    print(decrypted.decode())