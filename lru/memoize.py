from collections import OrderedDict
from functools import wraps

def lru_memoize(maxsize=128):
    def decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)  
                return cache[args]
            
            result = func(*args)
            cache[args] = result
            
            if len(cache) > maxsize:
                cache.popitem(last=False)  
            
            return result
        return wrapper
    return decorator

@lru_memoize(maxsize=3)
def slow_square(x):
    print(f"Computing square of {x}")
    return x * x

print(slow_square(2)) 
print(slow_square(3))  
print(slow_square(2)) 
print(slow_square(4)) 
print(slow_square(5))  
print(slow_square(3))  