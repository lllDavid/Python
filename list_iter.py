class ListIter:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0  
    
    def __iter__(self):
        return self  
    
    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration  
        value = self.lst[self.index]
        self.index += 1
        return value
    
my_list = [1, 2, 3, 4, 5]
it = ListIter(my_list)

print(next(it))  
print(next(it)) 
print(next(it))
print(next(it))  
print(next(it))  