person = {"name": "Alice", "age": 30, "city": "New York"}

name, city = person["name"], person["city"]

print(f"name={name}, city={city}")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(f"merged_dict={merged_dict}")

dict3 = {"e": 5, "f": 6}
all_merged = {**dict1, **dict2, **dict3}
print(f"all_merged={all_merged}")

dict4 = {"a": 100, "g": 7}
merged_overlap = {**dict1, **dict4} 
print(f"merged_overlap={merged_overlap}")

def function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

function(1, 2, 3, name="Alice", age=30)

function()

function(city="New York", country="USA")

args_list = [10, 20, 30]
kwargs_dict = {"color": "blue", "shape": "circle"}

function(*args_list, **kwargs_dict)
