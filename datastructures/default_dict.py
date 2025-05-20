from collections import defaultdict

default_dict = defaultdict(int)

default_dict['a'] += 1 
print("Default Dict with int:", default_dict)

default_list_dict = defaultdict(list)
default_list_dict['b'].append(2)  
print("Default Dict with list:", default_list_dict)

def default_factory():
    return "Default Value"

default_custom_dict = defaultdict(default_factory)
print("Custom Default Dict:", default_custom_dict['c'])

default_dict['x'] = 10
default_dict['y'] = 20
for key, value in default_dict.items():
    print(f"Key: {key}, Value: {value}")