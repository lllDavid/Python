# dict
person = {"name": "Alice", "age": 30, "city": "New York"}

name, city = person["name"], person["city"]

print(f"name={name}, city={city}")


# merge
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(f"merged_dict={merged_dict}")

# func
def function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

function(1, 2, 3, name="Alice", age=30)

