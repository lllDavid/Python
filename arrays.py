
import time
import numpy as np

def square_with_list(data):
    return [x**2 for x in data]

def square_with_numpy(data):
    return data**2

size = 10**7
data_list = list(range(size))
data_numpy = np.array(range(size))

start_time = time.time()
square_with_list(data_list)
list_time = time.time() - start_time

start_time = time.time()
square_with_numpy(data_numpy)
numpy_time = time.time() - start_time

print(f"Time list: {list_time:.5f} seconds")
print(f"Time array: {numpy_time:.5f} seconds")
