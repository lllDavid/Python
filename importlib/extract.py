def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

class Extractor:
    def __init__(self, data):
        self.data = data

    def extract_uppercase(self):
        return [char for char in self.data if char.isupper()]

some_variable = 42
another_variable = "Sample text"
