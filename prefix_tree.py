class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_end_of_word

    def starts_with(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))  
print(trie.search("app"))    
print(trie.search("appl"))   
print(trie.starts_with("ap")) 
print(trie.starts_with("banana")) 