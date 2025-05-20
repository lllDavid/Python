byte_arr = bytearray([65, 66, 67, 68, 69])

byte_arr.extend([70, 71, 72])
print("After extend:", byte_arr)

byte_arr.insert(0, 64)
print("After insert:", byte_arr)

byte_arr.remove(66)
print("After remove 66:", byte_arr)

popped = byte_arr.pop(2)
print("Popped byte:", popped)
print("After pop:", byte_arr)

slice_part = byte_arr[1:4]
print("Sliced part:", slice_part)

byte_arr.clear()
print("After clear:", byte_arr)

print("Length:", len(byte_arr))
