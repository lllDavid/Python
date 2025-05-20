my_tuple = ("122.223.442.23", "323.5345.22.115")

print(my_tuple[0])
print("122.223.442.23" in my_tuple)
print(len(my_tuple))

new_tuple = my_tuple + ("192.168.0.1", "10.0.0.1")
print(new_tuple)

repeated_tuple = my_tuple * 2
print(repeated_tuple)

print(my_tuple[1:])
print(my_tuple[:1])

for ip in my_tuple:
    print(ip)

ip1, ip2 = my_tuple
print(ip1, ip2)

print(my_tuple.index("323.5345.22.115"))

print(my_tuple.count("122.223.442.23"))

nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2][1])

try:
    my_tuple[0] = "new.ip.address"
except TypeError as e:
    print("Error:", e)

single_element_tuple = ("single",)
print(type(single_element_tuple))
