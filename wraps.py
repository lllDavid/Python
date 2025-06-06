from functools import wraps

def log_function_call(func):
    @wraps(func)  
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(3, 5)

print(f"Function name: {add.__name__}")
print(f"Function docstring: {add.__doc__}")