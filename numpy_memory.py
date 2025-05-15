import numpy as np

shape = (5, 100, 100)
data = np.random.randint(0, 256, size=shape, dtype=np.uint8)

mv = memoryview(data)

print("Original Data (first slice):")
print(mv[0])

mv[0] = mv[0] * 2

print("\nData after modification (first slice):")
print(data[0])

subview = mv[2:4, 30:70, 40:80]
print("\nSubview (slices of data from layers 2-3 and rows 30-70, cols 40-80):")
print(subview)

subview[:] = subview * 0

print("\nData after modifying the subview (layers 2-3, rows 30-70, cols 40-80):")
print(data[2:4, 30:70, 40:80])

import time

start_time = time.time()
copy_data = np.copy(data)
elapsed_time = time.time() - start_time
print(f"\nTime taken to copy data (without memoryview): {elapsed_time:.6f} seconds")

start_time = time.time()
mv_view = memoryview(data)
elapsed_time = time.time() - start_time
print(f"Time taken to create a memoryview (no copy): {elapsed_time:.6f} seconds")
