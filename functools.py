from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)  
cube = partial(power, exponent=3)  

print(square(4))  
print(cube(3))  

from functools import wraps

def my_decorator(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Says hello"""
    return f"Hello, {name}!"

print(greet("Alice"))  
print(greet.__name__)  
print(greet.__doc__)  

from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

alice = Student("Alice", 90)
bob = Student("Bob", 85)

print(alice > bob)  
print(alice <= bob)  



