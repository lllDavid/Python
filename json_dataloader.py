class json_loader:
    def __init__(self, filepath, batch_size=1):
        self.filepath = filepath
        self.batch_size = batch_size
        self.data = self._load_data()

    def _load_data(self):
        with open(self.filepath, 'r') as f:
            data = [line.strip().split() for line in f]
        return data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch

loader = json_loader('data.json', batch_size=2)

for batch in loader:
    print("Batch:", batch)