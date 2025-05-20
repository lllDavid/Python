class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    
    def size(self):
        return len(self.items)

q = Queue()

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print(q.size())  

print(q.dequeue())  
print(q.dequeue())  

print(q.size())  

print(q.is_empty())  

print(q.dequeue())  
print(q.is_empty())  
