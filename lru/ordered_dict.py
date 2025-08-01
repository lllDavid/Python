from collections import OrderedDict
import time

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            evicted = self.cache.popitem(last=False)
            print(f"Evicted: {evicted[0]}")

def fetch_user_profile(user_id):
    print(f"Fetching user {user_id}...")
    time.sleep(1)  
    return {"id": user_id, "name": f"User{user_id}"}

cache = LRUCache(3)

def get_profile(user_id):
    profile = cache.get(user_id)
    if profile:
        print(f"Cache hit for {user_id}")
        return profile
    print(f"Cache miss for {user_id}")
    profile = fetch_user_profile(user_id)
    cache.put(user_id, profile)
    return profile

for uid in [1, 2, 3, 2, 4, 1, 5]:
    print(get_profile(uid))
    print(f"Cache: {list(cache.cache.keys())}\n")