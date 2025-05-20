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

dq.extend([4, 5, 6])
print(dq)

dq.extendleft([-2, -1])
print(dq)

count_2 = dq.count(2)
print("Count of 2:", count_2)

dq.clear()
print(dq)

dq2 = deque(maxlen=3)
dq2.extend([1, 2, 3])
print(dq2)
dq2.append(4)
print(dq2)

dq3 = deque([10, 20, 30])
print(dq3[1])
