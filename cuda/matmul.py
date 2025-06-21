import numpy as np
from numba import cuda

@cuda.jit
def matmul_kernel(A, B, C):
    row, col = cuda.grid(2)
    if row < C.shape[0] and col < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[row, k] * B[k, col]
        C[row, col] = tmp

N = 16

A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)
C = np.zeros((N, N), dtype=np.float32)

threads_per_block = (16, 16)
blocks_per_grid_x = (C.shape[0] + threads_per_block[0] - 1) // threads_per_block[0]
blocks_per_grid_y = (C.shape[1] + threads_per_block[1] - 1) // threads_per_block[1]
blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

matmul_kernel[blocks_per_grid, threads_per_block](A, B, C)

print(C)