class MyCollection:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Handle slicing with bounds checking
            start, stop, step = key.indices(len(self.data))
            return [self.data[i] for i in range(start, stop, step)]
        elif isinstance(key, int):
            # Handle index access
            return self.data[key]
        else:
            raise KeyError("Invalid key type")

# Example usage:
obj = MyCollection([1, 2, 3, 4, 5])
print(obj[2])      # Output: 3
print(obj[1:4:2])  # Output: [2, 4]

class Calculator:
    def __init__(self, value):
        self.value = value
        
    def __call__(self, *args, **kwargs):
        if args:
            return self.value + sum(args)
        return self.value

# Example usage:
calc = Calculator(10)
print(calc(5, 10))  # Output: 25 (10 + 5 + 10)
print(calc())       # Output: 10
