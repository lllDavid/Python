import hashlib

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def merkle_tree(leaves):
    if len(leaves) == 0:
        return None

    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1])

    nodes = [sha256(leaf.encode() if isinstance(leaf, str) else leaf) for leaf in leaves]

    while len(nodes) > 1:
        temp_nodes = []
        for i in range(0, len(nodes), 2):
            combined = (nodes[i] + nodes[i+1]).encode()
            temp_nodes.append(sha256(combined))
        nodes = temp_nodes

        if len(nodes) % 2 == 1 and len(nodes) != 1:
            nodes.append(nodes[-1])

    return nodes[0]

data_blocks = ['a', 'b', 'c', 'd']
root_hash = merkle_tree(data_blocks)
print('Merkle Root:', root_hash)