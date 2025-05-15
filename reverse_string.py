def reverse(s):
    s1 = ""
    length = len(s) -1 
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

print(reverse("hello"))

s = "hello"
reversed_s = s[::-1]
print(reversed_s)  

s = "hello"
reversed_s = ''.join(reversed(s))
print(reversed_s)  