# str.maketrans()
# # Create a translation table to replace vowels with numbers
trans = str.maketrans("aeiou", "12345")
text = "hello"
print(text.translate(trans))  # Output: h2ll4

# str.translate()
# Remove vowels by translating them to None
trans = str.maketrans("", "", "aeiou")
text = "hello world"
print(text.translate(trans))  # Output: hll wrld

# str.center(width, fillchar)
"hello"
print(text.center(10, "-"))  # Output: "--hello---"

# str.lstrip([chars]
text = "   hello"
print(text.lstrip())  # Output: "hello"

text = "xxxyhello"
print(text.lstrip("xy"))  # Output: "hello" (removes 'x' and 'y')

#str.isspace()
text = "   "
print(text.isspace())  # Output: True

text = "hello"
print(text.isspace())  # Output: False
