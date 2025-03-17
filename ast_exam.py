import ast

def analyze_code(source_code):
    tree = ast.parse(source_code)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            args = [arg.arg for arg in node.args.args]
            decorators = [d.id for d in node.decorator_list if isinstance(d, ast.Name)]
            docstring = ast.get_docstring(node)
            print(f"Function: {func_name}, Arguments: {args}, Decorators: {decorators}, Docstring: {docstring}")
        elif isinstance(node, ast.ClassDef):
            class_name = node.name
            bases = [b.id for b in node.bases if isinstance(b, ast.Name)]
            print(f"Class: {class_name}, Bases: {bases}")
        elif isinstance(node, ast.Assign):
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            print(f"Assignment: {targets}")

if __name__ == "__main__":
    code = '''class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        """Returns a greeting message."""
        return f"Hello, {self.name}!"

@staticmethod
def add(a, b):
    return a + b
'''

    analyze_code(code)
