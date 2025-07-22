import hashlib

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def create_hash_chain(data_list):
    chain = []
    previous_hash = '0' * 64  

    for data in data_list:
        combined = previous_hash + data
        current_hash = sha256(combined.encode())
        chain.append(current_hash)
        previous_hash = current_hash

    return chain

data_blocks = [
    "Block 1 data",
    "Block 2 data",
    "Block 3 data",
    "Block 4 data"
]

hash_chain = create_hash_chain(data_blocks)

for i, h in enumerate(hash_chain):
    print(f"Hash {i+1}: {h}")