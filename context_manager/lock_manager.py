import threading

class Manager:
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()
        print("Lock acquired")
        return self.lock

    def __exit__(self, exc_type, exc_value, traceback):
        self.lock.release()
        print("Lock released")
        if exc_type:
            print(f"Exception caught: {exc_type.__name__}")
        return False 

lock = threading.Lock()

print("Normal execution")
with Manager(lock):
    print("Inside critical section")

print("\nException inside critical section")
try:
    with Manager(lock):
        print("Inside critical section")
        raise ValueError("Something went wrong")
except ValueError as e:
    print(f"Caught exception outside: {e}")