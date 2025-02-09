username = "David"
email = "david@gmail.com"
password = 123456

# Create
dict1 = {"Username:":username, "Email":email, "Password:":password}
# Update
age = 23
dict1.update({"Age":age})
# Print
print(dict1)
# Print
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

