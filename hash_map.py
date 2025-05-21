my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

hash_map = {}

hash_map['apple'] = 1
hash_map['banana'] = 2
hash_map['orange'] = 3

print(hash_map['banana'])  

print(len(hash_map))  

hash_map.pop('apple')

def two_sum(nums, target):
    num_map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], index]  
        
        num_map[num] = index
    
    return [] 

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  

