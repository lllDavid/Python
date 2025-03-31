class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, index):
        parent_idx = self.parent(index)
        
        if index > 0 and self.heap[index] < self.heap[parent_idx]:
            self.swap(index, parent_idx)
            self.heapify_up(parent_idx)
    
    def heapify_down(self, index):
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        size = len(self.heap)
        
        if left < size and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < size and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if min_index != index:
            self.swap(index, min_index)
            self.heapify_down(min_index)
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        
        return min_val
    
    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def is_empty(self):
        return len(self.heap) == 0

if __name__ == "__main__":
    heap = MinHeap()
    
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)
    
    print("Heap:", heap.heap)  
    
    print("Extract min:", heap.extract_min())  
    print("Extract min:", heap.extract_min())  
    print("Remaining heap:", heap.heap)