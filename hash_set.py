my_set = {1, 2, 3, 4}

another_set = set([1, 2, 3, 4])

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b 

intersection_set = set_a & set_b  

difference_set = set_a - set_b  

symmetric_difference_set = set_a ^ set_b  

numbers = {1, 2, 3, 4, 5}

numbers.add(6)

numbers.discard(3)

if 4 in numbers:
    print("4 is in the set")

even_numbers = {2, 4, 6, 8}
all_numbers = numbers | even_numbers 

print(all_numbers)  
