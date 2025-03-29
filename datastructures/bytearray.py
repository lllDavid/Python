# Creating a bytearray from a list of integers
byte_arr = bytearray([65, 66, 67, 68, 69])
print("Bytearray:", byte_arr)

# Modifying a byte in the array
byte_arr[0] = 97  
print("Modified Bytearray:", byte_arr)

# Converting bytearray to string
string_rep = byte_arr.decode('utf-8')
print("String Representation:", string_rep)

# Creating a bytearray from a string
byte_arr2 = bytearray("Hello", 'utf-8')
print("Bytearray from string:", byte_arr2)

# Appending a byte to the bytearray
byte_arr2.append(33)  
print("Appended Bytearray:", byte_arr2)

# Converting back to bytes
bytes_obj = bytes(byte_arr2)
print("Bytes object:", bytes_obj)
