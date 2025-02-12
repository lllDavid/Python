class Node:
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None    # Left child
        self.right = None   # Right child

class BST:
    def __init__(self):
        self.root = None  # Initially, the tree is empty

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  # Create the root if the tree is empty
        else:
            self._insert(self.root, value)  # Otherwise, insert recursively

    def _insert(self, node, value):
        # Recursively find the correct spot for the new value
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # Insert as the left child
            else:
                self._insert(node.left, value)  # Continue down the left side
        else:
            if node.right is None:
                node.right = Node(value)  # Insert as the right child
            else:
                self._insert(node.right, value)  # Continue down the right side

    def inorder(self):
        # Helper function to perform in-order traversal
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)  # Visit left child
            print(node.value, end=" ")  # Print node value
            self._inorder(node.right)  # Visit right child

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# In-order traversal (prints sorted values)
bst.inorder()  # Output: 20 30 40 50 60 70 80
