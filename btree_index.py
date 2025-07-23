class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return True
        if self.leaf:
            return False
        return self.children[i].search(k)

    def insert(self, k):
        if self.leaf:
            self.keys.append(k)
            self.keys.sort()
        else:
            i = 0
            while i < len(self.keys) and k > self.keys[i]:
                i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split(i)
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert(k)

    def split(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t)

    def insert(self, k):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, False)
            s.children.append(r)
            s.split(0)
            self.root = s
        self.root.insert(k)

    def search(self, k):
        return self.root.search(k)

bt = BTree(t=2)
for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    bt.insert(key)

for k in [6, 15, 17]:
    print(f"Key {k} found? {bt.search(k)}")