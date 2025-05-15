trans = str.maketrans("aeiou", "12345")
text = "hello"
print(text.translate(trans))

trans = str.maketrans("", "", "aeiou")
text = "hello world"
print(text.translate(trans))

print(text.center(10, "-"))

text = "   hello"
print(text.lstrip())

text = "xxxyhello"
print(text.lstrip("xy"))

text = "   "
print(text.isspace())

text = "hello"
print(text.isspace())

s = "apple:banana:cherry"
before, sep, after = s.partition(':')
print(before, sep, after)

s = "Hello\tWorld"
print(s.expandtabs(4))

print("hello".upper())

print("HELLO".lower())

print("hello world".title())

print("HeLLo WoRLD".swapcase())

print("abc".isalpha())

print("123".isdigit())

print("abc123".isalnum())

print("file.txt".endswith(".txt"))

print("I am Human".replace("Human", "Robot"))

print("one,two,three".split(","))
