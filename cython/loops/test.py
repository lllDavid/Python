from time import perf_counter
from cyt_func import c_function
from py_func import p_function

def test_slow_function():
    start = perf_counter()
    p_function(1000000)
    end = perf_counter()
    print(f"Slow function execution time: {end - start} seconds")

def test_fast_function():
    start = perf_counter()
    c_function(1000000)
    end = perf_counter()
    print(f"Fast function execution time: {end - start} seconds")

test_slow_function()
test_fast_function()
