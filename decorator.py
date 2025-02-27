import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("Before the function is called.")
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            result = None
        
        end_time = time.time()
        print(f"After the function is called. Execution time: {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@my_decorator
def say_hello(name, greeting="Hello"):
    if name == "error":
        raise ValueError("This is a test error.")
    print(f"{greeting}, {name}!")

say_hello("Alice", greeting="Hi")
say_hello("error")
