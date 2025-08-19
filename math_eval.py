import math

glbs = {
    '__builtins__': None,  
    'abs': abs,
    'round': round,
    'pow': pow,
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'log': math.log,
    'pi': math.pi,
    'e': math.e
}

def calc(expr):
    try:
        result = eval(expr, glbs)
        return result
    except Exception as e:
        return f"Error: {e}"

while True:
    expr = input("Enter expression (or 'q' to quit): ")
    if expr.lower() == 'q':
        break
    print("Result:", calc(expr))