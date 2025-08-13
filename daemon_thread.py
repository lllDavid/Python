import threading
import time
from datetime import datetime, timedelta
# Simulated workflow
class Cache:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def set(self, key, value, ttl_seconds):
        expiry = datetime.now() + timedelta(seconds=ttl_seconds)
        with self.lock:
            self.data[key] = (value, expiry)

    def get(self, key):
        with self.lock:
            item = self.data.get(key)
            if not item:
                return None
            value, expiry = item
            if expiry < datetime.now():
                del self.data[key]
                return None
            return value

    def cleanup(self):
        with self.lock:
            now = datetime.now()
            expired_keys = [k for k, (_, expiry) in self.data.items() if expiry < now]
            for k in expired_keys:
                print(f"Cleaning up expired cache key: {k}")
                del self.data[k]

def cache_cleanup_task(stop_event, cache, interval=5):
    while not stop_event.is_set():
        cache.cleanup()
        time.sleep(interval)
    print("Cache cleanup daemon stopped.")

if __name__ == "__main__":
    stop_event = threading.Event()
    cache = Cache()

    cache.set("key1", "value1", ttl_seconds=3)
    cache.set("key2", "value2", ttl_seconds=10)

    daemon_thread = threading.Thread(target=cache_cleanup_task, args=(stop_event, cache), daemon=True)
    daemon_thread.start()

    try:
        for i in range(12):
            print(f"Main program running... {i}")
            time.sleep(1)
    finally:
        print("Stopping daemon thread.")
        stop_event.set()
        daemon_thread.join()
        print("Program exiting.")