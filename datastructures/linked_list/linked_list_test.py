
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
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

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:  # Special case: if the head is the node to delete
            self.head = current.next
            current = None
            return
        # Search for the node to delete
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:  # Node not found
            return
        # Remove the node
        prev.next = current.next
        current = None

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create the LinkedList object
linked_list = LinkedList()

# Append elements to the list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Print the list
linked_list.print_list()  # 1 -> 2 -> 3 -> 4 -> 5 -> None

# Insert at the beginning
linked_list.insert_at_beginning(0)
linked_list.print_list()  # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

# Delete a node with data 3
linked_list.delete_node(3)
linked_list.print_list()  # 0 -> 1 -> 2 -> 4 -> 5 -> None

# Find a node with data 4
found_node = linked_list.find(4)
if found_node:
    print(f"Node with data {found_node.data} found.")
else:
    print("Node not found.")

# Get the length of the list
print("Length of the list:", linked_list.get_length())  # Length of the list: 4

# Reverse the list
linked_list.reverse()
linked_list.print_list()  # 5 -> 4 -> 2 -> 1 -> 0 -> None
