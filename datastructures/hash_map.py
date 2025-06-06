class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for idx, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index][idx] = (key, value)
                return
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None
    
    def remove(self, key):
        index = self._hash(key)
        for idx, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][idx]
                return

hmap = HashMap()

hmap.insert("apple", 10)
hmap.insert("banana", 20)
hmap.insert("orange", 30)

print(hmap.get("apple"))    
print(hmap.get("banana"))  
print(hmap.get("grape"))    

hmap.remove("banana")
print(hmap.get("banana"))   

hmap.insert("apple", 15)  
print(hmap.get("apple"))    
