#Create
my_set = {"david","mark","daniel","tim"}

# Update
my_set.add("melan")

# Delete
my_set.remove("mark")

# Access value
print("mark" in my_set)

for i in my_set:
    print(i)

# Set comprehension
my_set2 = {entry.upper() for entry in my_set}
for i in my_set2:
    print(i)




