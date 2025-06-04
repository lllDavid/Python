import ctypes
# CPython specific

nums = [10, 20, 30, 40, 50]

print("Raw object memory addresses")
for i, num in enumerate(nums):
    print(f"nums[{i}] = {num}, id = {id(num)}")

array_type = ctypes.py_object * len(nums)

c_array = array_type(*[ctypes.py_object(num) for num in nums])

print("\nAccessing c_array")
for i in range(len(nums)):
    obj_ptr = c_array[i]
    print(f"Pointer at index {i} -> object = {obj_ptr}, id = {id(obj_ptr)}")

print("\nAccessing specific index (e.g., nums[3])")
print(f"nums[3] = {nums[3]}")

print("\nArithmetic and ID")
result = nums[0] + 4 * 5
print(f"nums[0] + 4 * 5 = {result}, id = {id(result)}")