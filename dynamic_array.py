class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError('Index out of bounds')

    def append(self, value):
        if self.size == self.capacity:
            self._grow()
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError('Index out of bounds')
        if self.size == self.capacity:
            self._grow()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.size += 1

    def _grow(self):
        new_capacity = self.capacity * 2
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return '[' + ', '.join(str(self.array[i]) for i in range(self.size)) + ']'

if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(arr)

    arr.insert(1, 15)
    print(arr)

    print(arr[2])
    print(len(arr))