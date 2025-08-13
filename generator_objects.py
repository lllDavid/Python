class NumberCollection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def number_generator(self):
        for number in range(self.start, self.end + 1):
            yield number

collection = NumberCollection(1, 5)

for number in collection.number_generator():
    print(number)