import importlib.util

module_name = "extract"
module_path = "extract.py"

spec = importlib.util.spec_from_file_location(module_name, module_path)

module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

print(dir(module))  

from importlib.machinery import SourceFileLoader

loader = SourceFileLoader("extract", "extract.py")

code_obj = loader.get_code("extract")

print(code_obj)  
print(type(code_obj))  
