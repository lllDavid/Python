import math
import hashlib

class Filter:
    def __init__(self, n, p):
        """
        n : int - expected number of items
        p : float - false positive probability
        """
        self.n = n
        self.fp_prob = p
        self.size = self._get_size(n, p)
        self.hash_count = self._get_hash_count(self.size, n)
        self.bit_array = [0] * self.size

    def _get_size(self, n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def _get_hash_count(self, m, n):
        k = (m / n) * math.log(2)
        return int(k)

    def _hashes(self, item):
        hashes = []
        hash1 = int(hashlib.sha256(item.encode()).hexdigest(), 16)
        hash2 = int(hashlib.sha256((item + "salt").encode()).hexdigest(), 16)
        for i in range(self.hash_count):
            combined_hash = (hash1 + i * hash2) % self.size
            hashes.append(combined_hash)
        return hashes


    def add(self, item):
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def check(self, item):
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))

n = 20  
p = 0.05  

f = Filter(n, p)
print("Size of array: {}".format(f.size))
print("False positive Probability: {}".format(f.fp_prob))

items_to_add = ["python", "java", "golang", "rust", "javascript"]
items_to_check = ["python", "csharp", "ruby", "golang", "typescript"]

for item in items_to_add:
    f.add(item)

print("Checking membership with programming languages:")
for item in items_to_check:
    result = f.check(item)
    print(f"{item}: {'Possibly in set' if result else 'Definitely not in set'}")