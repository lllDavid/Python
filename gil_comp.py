import threading
import time

COUNT = 10_000_000

def countdown(n):
    while n > 0:
        n -= 1

t1 = threading.Thread(target=countdown, args=(COUNT // 2,))
t2 = threading.Thread(target=countdown, args=(COUNT // 2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"Threading Time: {end - start:.2f} seconds")

###

import multiprocessing

def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))
    p2 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))

    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()

    print(f"Multiprocessing Time: {end - start:.2f} seconds")