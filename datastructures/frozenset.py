my_frozenset = frozenset([1, 2, 3, 4, 5])

print("Original frozenset:", my_frozenset)

print(3 in my_frozenset)  
print(6 in my_frozenset)  

try:
    my_frozenset.add(6)
except AttributeError as e:
    print("Error:", e)  

another_frozenset = frozenset([4, 5, 6, 7])

union_frozenset = my_frozenset | another_frozenset
print("Union:", union_frozenset)  

intersection_frozenset = my_frozenset & another_frozenset
print("Intersection:", intersection_frozenset) 

difference_frozenset = my_frozenset - another_frozenset
print("Difference:", difference_frozenset)  

symmetric_difference_frozenset = my_frozenset ^ another_frozenset
print("Symmetric Difference:", symmetric_difference_frozenset)  
