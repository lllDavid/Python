from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  

from functools import partial

def add(a, b):
    return a + b

add_10 = partial(add, 10) 
print(add_10(5))  

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

print(say_hello.__name__)  
print(say_hello.__doc__)   

from functools import singledispatch

@singledispatch
def greet(obj):
    print("Hello, generic object!")

@greet.register(str)
def _(obj):
    print(f"Hello, {obj}!")

@greet.register(int)
def _(obj):
    print(f"Hello, number {obj}!")

greet("Alice")  
greet(10)       
greet([1, 2, 3])  

from functools import cached_property

class MyClass:
    def __init__(self):
        self._value = 42

    @cached_property
    def value(self):
        print("Computing value...")
        return self._value

obj = MyClass()
print(obj.value)  
print(obj.value) 