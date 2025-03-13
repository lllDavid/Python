## exec

function_code = """
def dynamic_function(a, b):
    return a * b
"""

exec(function_code)

result = dynamic_function(5, 3)

print(f"The result of the dynamic function is: {result}")

# scope
x = 10

def outer_function():
    x = 20

    def inner_function():
        x = 30
        print(f"Inner function (local scope) x = {x}")

    inner_function()
    print(f"Outer function (enclosing scope) x = {x}")

outer_function()

print(f"Global scope x = {x}")

## eval 
expression = "3 * (4 + 5)"

result = eval(expression)

print(f"The result of the expression {expression} is: {result}")
## eval

x = 5
y = 10

expression = "x * y"

restricted_scope = {"x": 3, "y": 7}

result = eval(expression, restricted_scope)

print(f"The result of '{expression}' in the restricted scope is: {result}")
