from functools import singledispatch

@singledispatch
def format_data(data):
    return f"Unknown type: {type(data).__name__}"

@format_data.register(int)
def _(data):
    return f"Integer: {data:,}"

@format_data.register(float)
def _(data):
    return f"Float: {data:.2f}"

@format_data.register(str)
def _(data):
    return f"String: '{data}'"

@format_data.register(list)
def _(data):
    return f"List: [{', '.join(str(item) for item in data)}]"

print(format_data(1234))          
print(format_data(3.14159))       
print(format_data("Hello"))       
print(format_data([1, 2, 3]))     
print(format_data({"key": "val"})) 