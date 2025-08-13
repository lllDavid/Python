import hashlib

def hash_number(number, algorithm='sha256'):
    number_bytes = str(number).encode()

    if algorithm == 'sha256':
        hash_obj = hashlib.sha256(number_bytes)
    elif algorithm == 'md5':
        hash_obj = hashlib.md5(number_bytes)

    return hash_obj.hexdigest()

num = 123456789

sha256_hash = hash_number(num, 'sha256')
md5_hash = hash_number(num, 'md5')

print(f"SHA-256 hash of {num}: {sha256_hash}")
print(f"MD5 hash of {num}: {md5_hash}")