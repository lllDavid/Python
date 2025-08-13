import math

def evaluate_expression(expr: str, variables: dict):
    safe_globals = {
        "__builtins__": {},  
        "math": math,
        "abs": abs,
        "min": min,
        "max": max,
        "pow": pow
    }

    try:
        result = eval(expr, safe_globals, variables)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

expr = "math.sin(x) + math.log(y) * pow(2, z)"
variables = {
    "x": math.pi / 2,
    "y": 10,
    "z": 3
}

result = evaluate_expression(expr, variables)
print(f"Result: {result}")