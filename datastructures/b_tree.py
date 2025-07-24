class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.values = []          
        self.children = []
        self.leaf = leaf
        self.next = None          

    def is_full(self):
        return len(self.keys) >= 2 * self.t - 1


class BPlusTree:
    def __init__(self, t=2):
        self.root = BPlusTreeNode(t, leaf=True)
        self.t = t

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.leaf:
            for i, k in enumerate(node.keys):
                if k == key:
                    return node.values[i]
            return None
        else:
            for i, k in enumerate(node.keys):
                if key < k:
                    return self.search(key, node.children[i])
            return self.search(key, node.children[-1])

    def insert(self, key, value):
        root = self.root
        if root.is_full():
            new_root = BPlusTreeNode(self.t)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key, value)

    def _insert_non_full(self, node, key, value):
        if node.leaf:
            idx = 0
            while idx < len(node.keys) and key > node.keys[idx]:
                idx += 1
            node.keys.insert(idx, key)
            node.values.insert(idx, value)
        else:
            idx = 0
            while idx < len(node.keys) and key > node.keys[idx]:
                idx += 1
            child = node.children[idx]
            if child.is_full():
                self._split_child(node, idx)
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(node.children[idx], key, value)

    def _split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BPlusTreeNode(t, leaf=node.leaf)

        mid = t - 1
        parent.keys.insert(i, node.keys[mid])
        parent.children.insert(i + 1, new_node)

        new_node.keys = node.keys[mid:]
        node.keys = node.keys[:mid]

        if node.leaf:
            new_node.values = node.values[mid:]
            node.values = node.values[:mid]
            new_node.next = node.next
            node.next = new_node
        else:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

    def print_leaves(self):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        while node:
            print(list(zip(node.keys, node.values)))
            node = node.next

tree = BPlusTree(t=3)

tree.insert("a", 1)
tree.insert("b", 2)
tree.insert("c", 3)
tree.insert("d", 4)
tree.insert("e", 5)
tree.insert("f", 6)

print(tree.search("c"))  
print(tree.search("z")) 

tree.print_leaves()      