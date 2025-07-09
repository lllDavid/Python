from inspect import getsource, signature

# Extract full source code and signature of a function from a Python module
# NOTE: Doesnt work with decorated and nested functions
def extract(file_path, func_name):
    try:
        with open(file_path, "r") as file:
            code = file.read()
        
        compiled = compile(code, file_path, 'exec')
        env = {}
        exec(compiled, env)
        
        if func_name in env:
            func_obj = env[func_name]
            source = getsource(func_obj)
            func_code = source.split("\n", 1)[1] if "\n" in source else ""
            func_params = str(signature(func_obj))
            return func_code, func_params
        else:
            print(f"Function {func_name} not found in {file_path}.")
            return None, None
    except Exception as e:
        print(f"Error extracting function {func_name}: {e}")
        return None, None
    
file_path = ""
func_name = ""

func_code, func_signature = extract(file_path, func_name)

print("Signature:", func_signature)
print("Code:")
print(func_code)