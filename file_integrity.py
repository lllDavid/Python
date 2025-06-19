import hashlib
import os

def check(file_path, hash_file, hash_algo='sha256'):
    if not os.path.exists(file_path):
        return False

    h = hashlib.new(hash_algo)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    current_hash = h.hexdigest()

    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            stored = f.readline().strip()
            if stored:
                stored_path, stored_hash = stored.split(':', 1)
                if stored_path == file_path and stored_hash == current_hash:
                    return True

    with open(hash_file, 'w') as f:
        f.write(f"{file_path}:{current_hash}\n")
    return False

file_path = 'text.txt'
hash_file = 'hash.txt'

if check(file_path, hash_file):
    print("No changes detected.")
else:
    print("File changed or no previous record.")
