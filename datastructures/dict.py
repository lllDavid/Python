username = "David"
email = "david@gmail.com"
password = 123456

dict1 = {"Username:": username, "Email": email, "Password:": password}

age = 23
dict1.update({"Age": age})

dict1.pop("Email")

print(dict1["Age"])

keys = dict1.keys()
print(keys)

values = dict1.values()
print(values)

for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

dict1 = {"1": 1, "2": 2, "3": 3}
dict2 = {v + 1 for v in dict1.values() if v > 2}
print(dict2)

dict1.clear()
print(dict1)

dict3 = dict.fromkeys(['a', 'b', 'c'], 0)
print(dict3)

print(dict3.get('b'))
print(dict3.get('d', 'Not Found'))

dict3.setdefault('d', 4)
print(dict3)

dict3.update({'a': 5, 'e': 6})
print(dict3)

print(len(dict3))

del dict3['e']
print(dict3)

print('a' in dict3)
print('z' in dict3)
