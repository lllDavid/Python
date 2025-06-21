from numba import cuda
import numpy as np
import math

@cuda.jit
def square_array(arr, out):
    idx = cuda.grid(1)  
    if idx < arr.size:  
        out[idx] = arr[idx] * arr[idx]

n = 1024

arr = np.random.rand(n).astype(np.float32)
out = np.zeros_like(arr)

d_arr = cuda.to_device(arr)
d_out = cuda.device_array_like(out)

threads_per_block = 256
blocks_per_grid = math.ceil(n / threads_per_block)

square_array[blocks_per_grid, threads_per_block](d_arr, d_out)

out = d_out.copy_to_host()

print("Input array (first 10):", arr[:10])
print("Squared array (first 10):", out[:10])