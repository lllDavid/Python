import time 
from cyt_func import c_function
from py_func import p_function

def test_slow_function():
    start = time.time()
    p_function(1000000)
    end = time.time()
    print(f"Slow function execution time: {end - start} seconds")

def test_fast_function():
    start = time.time()
    c_function(1000000)
    end = time.time()
    print(f"Fast function execution time: {end - start} seconds")

test_slow_function()
test_fast_function()
