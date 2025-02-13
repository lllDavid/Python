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

    
node = Node(6)
node.insert(5)
node.insert(2)
node.insert(4)
node.insert(1)
node.insert(2)
node.insert(4)
node.insert(19)
node.insert(29)
node.insert(11)
node.insert(4)
node.insert(2)

node.inorder_traversal()