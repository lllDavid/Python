class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.append(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.append(value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

    def find(self, value):
        if value < self.data:
            if self.left is None:
                return False
            return self.left.find(value)

        elif value > self.data:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True
        
node = Node(10)

node.append(1)
node.append(77)
node.append(3)
node.append(654)
node.append(2)

# Getting sorted values
print("Inorder:")
node.inorder()

# Copying or serializing 
print("\n""Preorder:")
node.preorder()

# Deleting a tree safely
print("\n""Postorder:")
node.postorder()