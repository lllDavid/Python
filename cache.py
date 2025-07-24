from functools import lru_cache, cached_property

# Example 1: LRU Cache
@lru_cache(maxsize=2)
def lru_cached_function(x):
    print(f"LRU Computing {x}...")
    return x * 2

print(lru_cached_function(5))  
print(lru_cached_function(10))
print(lru_cached_function(5))  
print(lru_cached_function(15)) 
print(lru_cached_function(10)) 

class MyClass:
    def __init__(self, x):
        self.x = x

    @cached_property
    def cached_property_function(self):
        print("Computing Property...")
        return self.x * 3

obj = MyClass(3)
print(obj.cached_property_function) 
print(obj.cached_property_function)  


# Manual
class Cache:
    def __init__(self, cache_size_bytes, line_size_bytes):
        self.line_size = line_size_bytes
        self.num_lines = cache_size_bytes // line_size_bytes
        self.cache = [None] * self.num_lines 
        self.hits = 0
        self.misses = 0

    def _get_index_tag(self, address):
        block_addr = address // self.line_size
        index = block_addr % self.num_lines
        tag = block_addr // self.num_lines
        return index, tag

    def read(self, address):
        index, tag = self._get_index_tag(address)
        entry = self.cache[index]
        if entry and entry[0] == tag:
            self.hits += 1
            return entry[1] 
        else:
            self.misses += 1
            data = f"Data@{address - (address % self.line_size)}"
            self.cache[index] = (tag, data)
            return data  

    def write(self, address, data):
        index, tag = self._get_index_tag(address)
        self.cache[index] = (tag, data)  

    def stats(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total) if total > 0 else 0
        return {"hits": self.hits, "misses": self.misses, "hit_rate": hit_rate}
    
cache = Cache(cache_size_bytes=64, line_size_bytes=16)

print(cache.read(0))    
print(cache.read(16))   
print(cache.read(0))    
cache.write(0, "NewData@0")
print(cache.read(0))    

print(cache.stats())