import random

class MyIterator:
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value <= 3:
            current_value = self.value
            self.value += 1
            return current_value
        else:
            raise StopIteration 

iter_obj = MyIterator()
for num in iter_obj:
    print(num)

class RandomNumberIterator:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated < self.count:
            self.generated += 1
            return random.randint(self.start, self.end)
        else:
            raise StopIteration

random_iter = RandomNumberIterator(1, 100, 5)
for num in random_iter:
    print(num)
