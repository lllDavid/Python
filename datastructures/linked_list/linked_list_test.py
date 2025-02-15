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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

node = Node(1)

node.append(2)
node.append(3)
node.append(4)
node.append(5)

node.print_list()