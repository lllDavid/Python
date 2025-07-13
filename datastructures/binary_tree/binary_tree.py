class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        return False

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:  
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_larger_node_value = self.right.find_min()
                self.value = min_larger_node_value
                self.right = self.right.delete(min_larger_node_value)
        return self

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def contains(self, value):
        return self.search(value)


node = Node(6)

values_to_insert = [5, 2, 4, 1, 2, 4, 19, 29, 11, 4, 2]
for val in values_to_insert:
    node.insert(val)

print("Inorder traversal:")
node.inorder_traversal() 

print("\nPreorder traversal:")
node.preorder_traversal()

print("\nPostorder traversal:")
node.postorder_traversal()

print("\nSearch for 19:", node.search(19))  
print("Search for 100:", node.search(100))  

print("\nContains 11:", node.contains(11))  
print("Contains 7:", node.contains(7))      

print("\nMinimum value:", node.find_min())  
print("Maximum value:", node.find_max())    

print("\nHeight of tree:", node.height())

print("\nDeleting 4...")
node = node.delete(4)
print("Inorder traversal after deleting 4:")
node.inorder_traversal()