import array

arr = array.array('i', [1, 2, 3, 4, 5])

print("Initial array:", arr)

print("First element:", arr[0])
print("Last element:", arr[-1])

arr[2] = 30
print("After modification:", arr)

arr.append(6)
print("After append:", arr)

arr.extend([7, 8, 9])
print("After extend:", arr)

arr.insert(0, 0)
print("After insert at start:", arr)

arr.remove(30)
print("After removing 30:", arr)

popped = arr.pop()
print("Popped element:", popped)
print("Array after pop:", arr)

index_8 = arr.index(8)
print("Index of 8:", index_8)

arr.append(8)
count_8 = arr.count(8)
print("Count of 8:", count_8)

lst = arr.tolist()
print("Array converted to list:", lst)

print("Iterating elements:")
for x in arr:
    print(x, end=' ')
print()

print("Buffer info:", arr.buffer_info())

arr.reverse()
print("Reversed array:", arr)

print("Typecode:", arr.typecode)
