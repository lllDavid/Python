import threading
import time
import random

counter = 0

def increment():
    global counter
    for _ in range(10000):  
        temp = counter
        time.sleep(random.uniform(0, 0.000001))  
        temp += 1
        counter = temp

threads = []
for _ in range(10):  
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)