# Create a byte object
data = bytearray(b"Hello, world!")

# Create a memoryview of the bytearray
mv = memoryview(data)

# Access the memoryview like a regular array
print(mv[0])  # Prints: 72 (ASCII value of 'H')
print(mv[1])  # Prints: 101 (ASCII value of 'e')

# Modify the data through the memoryview (it modifies the original data)
mv[0] = 74  # Change 'H' to 'J'

print(data)  # Prints: bytearray(b"Jello, world!")
