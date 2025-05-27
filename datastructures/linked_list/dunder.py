class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        self._size += 1

    def pop(self, index=None):
        if self._size == 0:
            raise IndexError("Pop from empty list")
        if index is None:
            index = self._size - 1
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            val = self.head.data
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            val = cur.next.data
            cur.next = cur.next.next
        self._size -= 1
        return val

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.data

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.data = value

    def __delitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self._size -= 1

    def __len__(self):
        return self._size

    def __contains__(self, item):
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __reversed__(self):
        def _reversed_nodes():
            stack = []
            cur = self.head
            while cur:
                stack.append(cur.data)
                cur = cur.next
            while stack:
                yield stack.pop()
        return _reversed_nodes()

    def __str__(self):
        return " -> ".join(str(item) for item in self)

    def __repr__(self):
        return f"LinkedList([{', '.join(repr(item) for item in self)}])"

ll = LinkedList([10, 20, 30])
print(ll)                
print(repr(ll))         

ll.append(40)
ll.insert(1, 15)
print(ll[1])             

ll[1] = 99
del ll[2]
print(99 in ll)          
print(len(ll))           

print(list(reversed(ll)))  

for value in ll:
    print(value, end=' ')  

print("\nPopped:", ll.pop())  
