class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, value):
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("After appending values:")
linked_list.print_list()  

linked_list.prepend(0)
print("After prepending 0:")
linked_list.print_list()  

linked_list.delete_with_value(2)
print("After deleting 2:")
linked_list.print_list()  

linked_list.delete_with_value(0)
print("After deleting 0 (head):")
linked_list.print_list() 
