import ctypes

buffer_size = 6
memory = (ctypes.c_int * buffer_size)()  

memory[0] = 10
memory[1] = 20
memory[2] = 30
memory[3] = 40
memory[4] = 50
memory[5] = 60

base_address = ctypes.addressof(memory)
print(f"Base address: {hex(base_address)}")  

offset = 3

int_size = ctypes.sizeof(ctypes.c_int)  
target_address = base_address + (offset * int_size)
print(f"Target address (offset {offset}): {hex(target_address)}")  

pointer = ctypes.cast(target_address, ctypes.POINTER(ctypes.c_int))
value = pointer[0]
print(f"Value at offset {offset}: {value}")  

pointer[0] = 99
print(f"Updated value at offset {offset}: {memory[offset]}")  

print("Updated memory:", [memory[i] for i in range(buffer_size)])