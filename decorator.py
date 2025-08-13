from time import perf_counter, sleep

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timeit
def train_model(epochs):
    for _ in range(epochs):
        sleep(0.1)

train_model(5)



import tracemalloc
import numpy as np

def mem_profiler(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        print(f"Peak memory usage: {peak / 10**6:.4f} MB")
        
        return result
    return wrapper

@mem_profiler
def train_dummy(epochs):
    data = []
    for _ in range(epochs):
        data.append(np.random.randn(1000, 100))
    return data

train_dummy(2)