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
