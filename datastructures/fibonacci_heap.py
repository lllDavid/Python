import math

class FibNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.count = 0

    def insert(self, key):
        node = FibNode(key)
        self._merge_with_root_list(node)
        if self.min is None or node.key < self.min.key:
            self.min = node
        self.count += 1
        return node

    def get_min(self):
        return self.min.key if self.min else None

    def extract_min(self):
        z = self.min
        if z:
            if z.child:
                children = [x for x in self._iterate(z.child)]
                for child in children:
                    self._merge_with_root_list(child)
                    child.parent = None

            self._remove_from_root_list(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.count -= 1
        return z.key if z else None

    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def _cut(self, x, y):
        self._remove_from_child_list(y, x)
        y.degree -= 1
        self._merge_with_root_list(x)
        x.parent = None
        x.mark = False

    def _cascading_cut(self, y):
        z = y.parent
        if z:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    def _consolidate(self):
        A = [None] * (int(math.log2(self.count)) + 1)
        nodes = [x for x in self._iterate(self.min)]

        for w in nodes:
            x = w
            d = x.degree
            while A[d]:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        self.min = None
        for node in A:
            if node:
                if not self.min or node.key < self.min.key:
                    self.min = node

    def _link(self, y, x):
        self._remove_from_root_list(y)
        y.left = y.right = y
        self._merge_with_child_list(x, y)
        y.parent = x
        x.degree += 1
        y.mark = False

    def _merge_with_root_list(self, node):
        if not self.min:
            node.left = node.right = node
        else:
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _merge_with_child_list(self, parent, node):
        if not parent.child:
            parent.child = node
            node.left = node.right = node
        else:
            child = parent.child
            node.left = child
            node.right = child.right
            child.right.left = node
            child.right = node

    def _remove_from_child_list(self, parent, node):
        if parent.child == node:
            if node.right != node:
                parent.child = node.right
            else:
                parent.child = None
        node.left.right = node.right
        node.right.left = node.left

    def _iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag:
                break
            flag = True
            yield node
            node = node.right

fib = FibonacciHeap()

n1 = fib.insert(10)
n2 = fib.insert(2)
n3 = fib.insert(15)

print(fib.get_min())    

fib.decrease_key(n3, 1)
print(fib.get_min())    

print(fib.extract_min()) 
print(fib.get_min())     