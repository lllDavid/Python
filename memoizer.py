import time
import functools

class MemoizedFunction:
    def __init__(self, func, cache_size=10, transform=None):
        self.func = func
        self.cache = {}
        self.cache_order = []
        self.cache_size = cache_size
        self.transform = transform if transform else lambda x: x  

    def __call__(self, *args, **kwargs):
        transformed_args = tuple(map(self.transform, args))  
        cache_key = (transformed_args, frozenset(kwargs.items()))  
        
        if cache_key in self.cache:
            print("Cache hit for:", transformed_args)
            return self.cache[cache_key]

        print("Computing result for:", transformed_args)
        result = self.func(*args, **kwargs)

        if len(self.cache) >= self.cache_size:
            oldest_key = self.cache_order.pop(0)
            del self.cache[oldest_key]

        self.cache[cache_key] = result
        self.cache_order.append(cache_key)

        return result

@MemoizedFunction
def slow_square(x):
    time.sleep(1)  
    return x * x

print(slow_square(4))  
print(slow_square(4))  
print(slow_square(5)) 
print(slow_square(5))  