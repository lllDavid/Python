class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next 
                current.next = new_node