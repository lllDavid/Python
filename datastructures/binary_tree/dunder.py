class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.insert(key)

    def find(self, key):
        if key == self.key:
            return True
        elif key < self.key and self.left:
            return self.left.find(key)
        elif key > self.key and self.right:
            return self.right.find(key)
        return False

    def inorder(self):
        if self.left:
            for val in self.left.inorder():
                yield val
        yield self.key
        if self.right:
            for val in self.right.inorder():
                yield val

    def _delete_node(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left._delete_node(key)
        elif key > self.key:
            if self.right:
                self.right = self.right._delete_node(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            
            self.key = min_larger_node.key
            self.right = self.right._delete_node(min_larger_node.key)
        return self

    def __repr__(self):
        left = repr(self.left) if self.left else ''
        right = repr(self.right) if self.right else ''
        return f"({left} {self.key} {right})".strip()


class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            self._size = 1
        else:
            if not self.__contains__(key):
                self.root.insert(key)
                self._size += 1

    def delete(self, key):
        if self.__contains__(key):
            self.root = self.root._delete_node(key)
            self._size -= 1

    def __contains__(self, key):
        if self.root is None:
            return False
        return self.root.find(key)

    def __iter__(self):
        if self.root:
            yield from self.root.inorder()

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.root is None:
            return "BST()"
        return f"BST{repr(self.root)}"


if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)

    print(bst)                
    print(7 in bst)           
    print(8 in bst)           
    print(list(bst))          
    print(len(bst))           

    bst.delete(5)
    print(bst)                
    print(list(bst))          
    print(len(bst))          
