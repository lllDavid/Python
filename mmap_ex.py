import mmap
import os

def create_file(filename, size_mb):
    with open(filename, 'wb') as f:
        chunk = b'abc123\n' * 1000 
        while f.tell() < size_mb * 1024 * 1024:
            f.write(chunk)

def search_and_replace(filename, search_bytes, replace_bytes):
    if len(search_bytes) != len(replace_bytes):
        raise ValueError("Search and replace bytes must be the same length")

    with open(filename, 'r+b') as f:
        size = os.path.getsize(filename)

        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mm:
            offset = 0
            while True:
                index = mm.find(search_bytes, offset)
                if index == -1:
                    break
                mm[index:index + len(search_bytes)] = replace_bytes
                offset = index + len(search_bytes)
            mm.flush()

if __name__ == "__main__":
    filename = "mmap_file.dat"
    if not os.path.exists(filename):
        create_file(filename, size_mb=10)

    search_and_replace(filename, b'abc123', b'ABCXYZ')