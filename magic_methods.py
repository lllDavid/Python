class Count:
    def __init__(self):
        self.value = 1

    def __add__(self, other):
        return self.value + other.value
    
    def count_up(self):
        self.value = self.value + 1
    
    def count_down(self):
        self.value = self.value - 1

count1 = Count()
count2 = Count()

print(count1+count2)

