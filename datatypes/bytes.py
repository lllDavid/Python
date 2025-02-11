# Creating a bytes object
b = bytes([65, 66, 67])  # Creates b'ABC' (ASCII values for 'A', 'B', and 'C')
print(b) 

# Creating a bytes object from a string (encoded as UTF-8 by default)
b_str = "hello".encode()  # Converts the string "hello" to bytes
print(b_str)  

# Decoding bytes back to a string
decoded_str = b_str.decode()  # Converts bytes back to the string "hello"
print(decoded_str)  

# Working with file data (binary files)
with open("image.png", "rb") as file:  # Open a file in binary read mode
    image_data = file.read()  
    print(image_data[:10])  
