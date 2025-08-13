class EvenNumbers:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_number:
            raise StopIteration
        else:
            number = self.current
            self.current += 2
            return number

evens = EvenNumbers(10)
for num in evens:
    print(num)