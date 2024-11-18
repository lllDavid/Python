def reverse(s):
    s1 = ""
    length = len(s) -1 
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

print(reverse("Hallo"))