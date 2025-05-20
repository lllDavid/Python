my_list = [1, 2, 3, 4, 5]

my_list.append(6)
my_list.insert(5, 6)

my_list.remove(5)
my_list.pop(0)

print(my_list[0])

print(my_list[0:])

print(my_list[::-1])

for i in my_list:
    print(i)

my_list2 = [i**2 for i in my_list if i > 3]
print(my_list2)

my_list.extend([7, 8, 9])
print(my_list)

my_list.count(6)
print(my_list.count(6))

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.clear()
print(my_list)

my_list = [3, 1, 4, 2, 5]
print(min(my_list))
print(max(my_list))

index_of_4 = my_list.index(4)
print(index_of_4)

my_list.reverse()
print(my_list)

copied_list = my_list.copy()
print(copied_list)

my_list += [6, 7]
print(my_list)
