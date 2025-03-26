from sys import getsizeof

# List
nums = []

print(getsizeof(nums),"Bytes") # 56 Bytes

nums = [1]

print(getsizeof(nums),"Bytes") # 64 Bytes, 8 Bytes added for pointer
print(getsizeof(nums[0]),"Bytes") # 28 Bytes, INT 

# Tuple
nums = ()

print(getsizeof(nums),"Bytes") # 40 Bytes

nums = (1,)

print(getsizeof(nums),"Bytes") # 48 Bytes, 8 Bytes added for pointer
print(getsizeof(nums[0]),"Bytes") # 28 Bytes, INT



# Dictionary
nums = {}

print(getsizeof(nums), "Bytes")  

nums = {1: 'a'}

print(getsizeof(nums), "Bytes")  
print(getsizeof(next(iter(nums.items()))), "Bytes")  

# Set
nums = set()

print(getsizeof(nums), "Bytes")  

nums = {1}

print(getsizeof(nums), "Bytes")  
print(getsizeof(next(iter(nums))), "Bytes")  
