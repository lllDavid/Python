from contextlib import contextmanager
import threading
import time
import random

class Connection:
    def __init__(self, id):
        self.id = id
        self.in_use = False

    def open(self):
        print(f"Connection {self.id} opened")

    def close(self):
        print(f"Connection {self.id} closed")

class ConnectionPool:
    def __init__(self, size):
        self._pool = [Connection(i) for i in range(size)]
        self._lock = threading.Lock()

    @contextmanager
    def acquire(self):
        conn = None
        with self._lock:
            for c in self._pool:
                if not c.in_use:
                    c.in_use = True
                    conn = c
                    break
        if conn is None:
            raise RuntimeError("No available connections")
        try:
            conn.open()
            yield conn
        finally:
            conn.close()
            with self._lock:
                conn.in_use = False

pool = ConnectionPool(10)

def worker(name):
    try:
        with pool.acquire() as conn:
            print(f"{name} acquired Connection {conn.id}")
            time.sleep(random.uniform(0.5, 1.5))  
            print(f"{name} releasing Connection {conn.id}")
    except RuntimeError as e:
        print(f"{name}: {e}")

import threading

threads = [threading.Thread(target=worker, args=(f"Worker-{i}",)) for i in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()