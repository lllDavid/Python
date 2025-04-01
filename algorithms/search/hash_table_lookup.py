data = {x: i for i, x in enumerate([10, 20, 30, 40, 50])}

def hash_lookup(data_dict, target):
    return data_dict.get(target, -1)  

print(hash_lookup(data, 30))  