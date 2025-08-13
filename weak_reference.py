import weakref

_cache = weakref.WeakValueDictionary()

class Data:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Data({self.value})"

def get_data(key):
    if key in _cache:
        print("Cache hit")
        return _cache[key]
    print("Cache miss")
    obj = Data(key)
    _cache[key] = obj
    return obj

d1 = get_data(10)  
d2 = get_data(10) 

del d1, d2  
import gc; gc.collect()

print("After GC, cache contains:", list(_cache.items()))