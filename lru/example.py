from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = set()
        self.order = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return key
        return -1

    def put(self, key: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            evicted = self.order.popleft()
            self.cache.remove(evicted)
        self.cache.add(key)
        self.order.append(key)

lru = LRUCache(2)
lru.put(1)
lru.put(2)
print(lru.get(1))  
lru.put(3)         
print(lru.get(2))  
