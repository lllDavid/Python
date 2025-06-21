from numba import cuda
import numpy as np
import math

@cuda.jit
def relu_kernel(x, out):
    idx = cuda.grid(1)
    if idx < x.size:
        out[idx] = max(0, x[idx])

n = 1024
x = np.random.randn(n).astype(np.float32)  
out = np.zeros_like(x)

d_x = cuda.to_device(x)
d_out = cuda.device_array_like(out)

threads_per_block = 256
blocks_per_grid = math.ceil(n / threads_per_block)

relu_kernel[blocks_per_grid, threads_per_block](d_x, d_out)

out = d_out.copy_to_host()

print("Input (first 10):", x[:10])
print("ReLU output (first 10):", out[:10])