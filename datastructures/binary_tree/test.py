class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_value(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert_value(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert_value(value)

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

node.insert_value(2)
node.insert_value(4)
node.insert_value(5)
node.insert_value(6)
node.insert_value(1)
node.insert_value(22)
node.insert_value(89)

node.inorder_traversal()

print(node.find_value(22))
print(node.find_value(999))