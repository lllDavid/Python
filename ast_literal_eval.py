import ast

def safe_eval(expr):
    try:
        result = ast.literal_eval(expr)
        return result
    except Exception as e:
        return f"Error: Unsafe or invalid expression - {e}"

print(safe_eval("[1, 2, 3]"))       
print(safe_eval("{'a': 1, 'b': 2}"))   
print(safe_eval("2 + 3"))               
print(safe_eval("__import__('os').system('rm -rf /')")) 