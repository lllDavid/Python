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
