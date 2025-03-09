import numpy as np

# Step 1: Create a large 3D NumPy array to simulate scientific data
shape = (5, 100, 100)  # A 3D array with 5 layers of 100x100 data points
data = np.random.randint(0, 256, size=shape, dtype=np.uint8)

# Step 2: Create a memoryview object that gives a view on this data
mv = memoryview(data)

# Step 3: Demonstrate accessing the memoryview directly (without copying data)
print("Original Data (first slice):")
print(mv[0])  # Print the first 2D slice of the 3D array

# Step 4: Let's apply a transformation — e.g., doubling the values in the first slice
mv[0] = mv[0] * 2

# Step 5: Check how the original NumPy array has been modified
print("\nData after modification (first slice):")
print(data[0])  # The first slice should be updated because memoryview directly modified the array

# Step 6: Demonstrating slicing with memoryview (viewing a subarray)
# Let's get a subview of the memoryview, representing a smaller part of the data
subview = mv[2:4, 30:70, 40:80]  # Subview of layers 2 and 3, rows 30-70, columns 40-80
print("\nSubview (slices of data from layers 2-3 and rows 30-70, cols 40-80):")
print(subview)

# Step 7: Modify the subview and observe the effect on the original array
subview[:] = subview * 0  # Set all values in the subview to zero

# Step 8: Check the original array again to see the changes
print("\nData after modifying the subview (layers 2-3, rows 30-70, cols 40-80):")
print(data[2:4, 30:70, 40:80])  # The corresponding portion of the original array should now be zero

# Step 9: Exploring performance benefits: Using `memoryview` on a large dataset instead of copying
import time

# Without memoryview (Copying the entire data to another array)
start_time = time.time()
copy_data = np.copy(data)  # Copying the entire array
elapsed_time = time.time() - start_time
print(f"\nTime taken to copy data (without memoryview): {elapsed_time:.6f} seconds")

# Using memoryview (No copy, just a view)
start_time = time.time()
mv_view = memoryview(data)  # Just a view, no copying
elapsed_time = time.time() - start_time
print(f"Time taken to create a memoryview (no copy): {elapsed_time:.6f} seconds")
