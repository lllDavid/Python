import ctypes

number = ctypes.c_int(42)

print(f"Value: {number.value}")
print(f"Memory Address: {ctypes.addressof(number)}")

number.value = 100
print(f"New Value: {number.value}")

array_type = ctypes.c_int * 5 
array = array_type(1, 2, 3, 4, 5)

for i in range(5):
    print(f"Array element {i}: {array[i]} at address {ctypes.addressof(array) + i * ctypes.sizeof(ctypes.c_int)}")