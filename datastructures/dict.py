username = "David"
email = "david@gmail.com"
password = 123456

# Create
dict1 = {"Username:":username, "Email":email, "Password:":password}

# Update
age = 23
dict1.update({"Age":age})

# Delete
dict1.pop("Email")

# Print
print(dict1)

# Access value by key
print(dict1["Age"])

# Get all keys
keys = dict1.keys()
print(keys)

# Get all values
values = dict1.values()
print(values)  

# Get all keys and values 
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

# Dictionary comprehension
dict1 = {"1":1, "2":2, "3":3}
dict2 = { v + 1 for v in dict1.values() if v > 2}
print(dict2)
