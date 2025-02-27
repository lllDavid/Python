n = [1,2,3,4,5,6,7]
t = 6

def find(n,t):
    start = 0
    end = len(n) - 1
    while start <= end:
        mid = (start+end) // 2
        if n[mid] == t:
            return mid
        elif n[mid] > t:
            end = mid -1
        elif n[mid] < t:
            start = mid + 1
        

print(find(n,t))

n = [1, 2, 3, 4, 5, 6, 7]
t = 6

def find2(n, t):
    start = 0
    end = len(n) - 1
    
    for _ in range(len(n)):
        if start > end:
            return -1  
        
        mid = (start + end) // 2
        
        if n[mid] == t:
            return mid
        elif n[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
            
    return -1  

print(find2(n, t))
