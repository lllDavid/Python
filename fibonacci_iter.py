class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > self.count:
            c = self.a + self.b
            self.a = self.b
            self.b = c
            self.count += 1
            return self.a
        else:
            raise StopIteration
        
fib_iter = FibonacciIterator(10)
for i in fib_iter:
    print(i)