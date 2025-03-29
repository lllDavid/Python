# Create a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])

# Display the frozenset
print("Original frozenset:", my_frozenset)

# Check membership
print(3 in my_frozenset)  
print(6 in my_frozenset)  

# Attempting to add an element
try:
    my_frozenset.add(6)
except AttributeError as e:
    print("Error:", e)  

# Set operations with frozenset
another_frozenset = frozenset([4, 5, 6, 7])

# Union of frozensets
union_frozenset = my_frozenset | another_frozenset
print("Union:", union_frozenset)  

# Intersection of frozensets
intersection_frozenset = my_frozenset & another_frozenset
print("Intersection:", intersection_frozenset) 

# Difference of frozensets
difference_frozenset = my_frozenset - another_frozenset
print("Difference:", difference_frozenset)  

# Symmetric difference of frozensets
symmetric_difference_frozenset = my_frozenset ^ another_frozenset
print("Symmetric Difference:", symmetric_difference_frozenset) 