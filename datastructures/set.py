my_set = {"david", "mark", "daniel", "tim"}

my_set.add("melan")

my_set.remove("mark")

print("mark" in my_set)

for i in my_set:
    print(i)

my_set2 = {entry.upper() for entry in my_set}
for i in my_set2:
    print(i)

my_set.discard("nonexistent") 

print(len(my_set))

my_set.clear()
print(my_set)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))

print(set_a.isdisjoint(set_b))
print(set_a.issubset({1, 2, 3, 4, 5}))
print(set_b.issuperset({3, 4}))
