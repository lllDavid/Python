#1)
iterable = [1, 2, 3, 4, 5] 

iterable=iter(iterable)     

print(next(iterable))      
print(next(iterable))
print(next(iterable))       


class iterator:
    iterable =[1,2,3,4,5,6,7,8,9,10]
    for iterator in iterable:
        print(iterator**2)

#2)
class Iterator:
  
    def __iter__(self):
        self.nummer = 1
        return self
    
    def __next__(self):
        if self.nummer<=10:
            quadrat=self.nummer*self.nummer
            self.nummer=self.nummer+1
            return quadrat
        else:
            raise StopIteration

quadrierteZahlen= Iterator()
for quadrat in quadrierteZahlen:
    print(quadrat)

#3)
class iter:
    def __iter__(self):
        self.num = 1
        self.wert = int(input("Range: "))
        return self
    def __next__(self):
        if self.num <= self.wert:
            quad = self.num**2
            self.num+=1
            return quad
        raise StopIteration

instance = iter()
for i in instance:
    print(i)


