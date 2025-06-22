import importlib

class ModuleImporter:
    @staticmethod
    def import_and_run(module_name, function_name, *args, **kwargs):
        mod = importlib.import_module(module_name)
        print("Module Name:", mod.__name__)
        func = getattr(mod, function_name)
        return func(*args, **kwargs)
    
m = ModuleImporter()
result = m.import_and_run("my_module", "add", 2, 3)
print("Result of imported function:", result)