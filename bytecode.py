import dis

def co_function(x, y):
    if x > y:
        z = x - y
    else:
        z = x + y
    
    result = 0
    for i in range(5):
        result += i
    
    return z + result

dis.dis(co_function)


# eval
def execute_expression(expr, context):
    try:
        result = eval(expr, {"__builtins__": {}}, context)
        return result
    except Exception as e:
        return f"Invalid expression: {e}"

dis.dis(execute_expression)


## list vs generator
def list_comp():
    return [x*x for x in range(10)]

def gen_expr():
    return (x*x for x in range(10))

print("List Comprehension:")
dis.dis(list_comp)

print("\nGenerator Expression:")
dis.dis(gen_expr)
