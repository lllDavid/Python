import inspect

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, function_info):
        self.stack.append(function_info)

    def pop(self):
        self.stack.pop()

    def __str__(self):
        return '\n'.join([str(item) for item in self.stack])

def example_func(a, b=2):
    c = a + b
    d:float = 3.14
    e = 0b1010 
    return c + d + e

sig = inspect.signature(example_func)
argspec = inspect.getfullargspec(example_func)
source = inspect.getsource(example_func)

func_info = {
    'name': example_func.__name__,
    'signature': str(sig),
    'argspec': argspec,
    'source': source
}

s = Stack()
print("Initial Stack:")
print(s)

s.push(func_info)
print("\nStack after pushing function info:")
print(s)