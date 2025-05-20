import heapq

class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def push(self, item, priority):
        heapq.heappush(self.pq, (priority, item))
    
    def pop(self):
        if self.pq:
            return heapq.heappop(self.pq)[1]
    
    def is_empty(self):
        return len(self.pq) == 0

pq = PriorityQueue()

pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)

while not pq.is_empty():
    task = pq.pop()
    print(task)
