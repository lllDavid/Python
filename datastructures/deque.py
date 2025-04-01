from collections import deque

dq = deque()

dq.append(1)           
dq.append(2)
dq.append(3)

dq.appendleft(0)       

print(dq)  

dq.pop()               
print(dq)  

dq.popleft()           
print(dq)  

dq.rotate(1)           
print(dq)  

dq.rotate(-1)          
print(dq)  
