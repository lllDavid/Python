import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

for _ in range(10):
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final counter value:", counter)
