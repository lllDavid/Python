class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None

    def add(self, val):
        branch = 'left' if val < self.val else 'right'
        node = getattr(self, branch)
        if node is None:
            setattr(self, branch, Node(val))
        elif val != self.val:
            node.add(val)

    def has(self, val):
        if val == self.val: return True
        next_node = self.left if val < self.val else self.right
        return next_node.has(val) if next_node else False

    def walk(self):
        if self.left: yield from self.left.walk()
        yield self.val
        if self.right: yield from self.right.walk()

    def remove(self, val):
        if val < self.val:
            if self.left: self.left = self.left.remove(val)
        elif val > self.val:
            if self.right: self.right = self.right.remove(val)
        else:
            if not self.left: return self.right
            if not self.right: return self.left
            min_node = self.right
            while min_node.left: min_node = min_node.left
            self.val = min_node.val
            self.right = self.right.remove(min_node.val)
        return self

    def __repr__(self):
        l = repr(self.left) if self.left else ''
        r = repr(self.right) if self.right else ''
        return f"({l} {self.val} {r})".strip()


class BST:
    def __init__(self):
        self.root, self.size = None, 0

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            self.size = 1
        elif val not in self:
            self.root.add(val)
            self.size += 1

    def delete(self, val):
        if val in self:
            self.root = self.root.remove(val)
            self.size -= 1

    def __contains__(self, val):
        return self.root.has(val) if self.root else False

    def __iter__(self):
        if self.root: yield from self.root.walk()

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"BST{repr(self.root)}" if self.root else "BST()"


if __name__ == "__main__":
    t = BST()
    for x in [10, 5, 15, 3, 7]: t.insert(x)

    print(t)
    print(7 in t)
    print(8 in t)
    print(list(t))
    print(len(t))

    t.delete(5)
    print(t)
    print(list(t))
    print(len(t))