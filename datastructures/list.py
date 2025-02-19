# Create
my_list = [1, 2, 3, 4, 5]

# Update
my_list.append(6)
my_list.insert(5,6)

# Delete
my_list.remove(5)
my_list.pop(0)

# Access a value
print(my_list[0])

# Print all values:
print(my_list[0:])

# Print all values in reverse:
print(my_list[::-1])

# Iterate over values
for i in my_list:
    print(i)

# List comprehension
my_list2 = [i**2 for i in my_list if i > 3]
