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

    def find_value(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find_value(value)
        
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find_value(value)
        
        else:
            return True


node = Node(10)
node.insert(2)
node.insert(4)
node.insert(8)
node.insert(7)
node.insert(1)

node.inorder_traversal()

print(node.find_value(4))