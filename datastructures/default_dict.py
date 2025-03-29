from collections import defaultdict

# Creating a defaultdict with default type as int
default_dict = defaultdict(int)

default_dict['a'] += 1 
print("Default Dict with int:", default_dict)

# Creating a defaultdict with default type as list
default_list_dict = defaultdict(list)
default_list_dict['b'].append(2)  
print("Default Dict with list:", default_list_dict)

# Creating a defaultdict with a custom default factory
def default_factory():
    return "Default Value"

default_custom_dict = defaultdict(default_factory)
print("Custom Default Dict:", default_custom_dict['c'])

# Iterating through a defaultdict
default_dict['x'] = 10
default_dict['y'] = 20
for key, value in default_dict.items():
    print(f"Key: {key}, Value: {value}")