# Create the tuple
my_tuple = ("122.223.442.23", "323.5345.22.115")

# Access value
print(my_tuple[0])  

# Check for membership
print("122.223.442.23" in my_tuple)  

# Get length of tuple
print(len(my_tuple))  

# Concatenate another tuple
new_tuple = my_tuple + ("192.168.0.1", "10.0.0.1")
print(new_tuple) 

# Repeat the tuple
repeated_tuple = my_tuple * 2
print(repeated_tuple)  

# Slicing the tuple
print(my_tuple[1:])  
print(my_tuple[:1])  

# Iterating through the tuple
for ip in my_tuple:
    print(ip)

# Tuple unpacking
ip1, ip2 = my_tuple
print(ip1, ip2)  
