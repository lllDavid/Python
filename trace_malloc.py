import tracemalloc

tracemalloc.start()

def example_function():
    a = [i for i in range(10000)]  
    b = [i * 2 for i in range(5000)]  

example_function()

current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 10**6} MB")
print(f"Peak memory usage: {peak / 10**6} MB")

tracemalloc.stop()
