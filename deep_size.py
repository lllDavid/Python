from random import randint
from sys import getsizeof
from time import sleep

def deep_getsizeof(obj, seen=None):
    size = getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(deep_getsizeof(v, seen) + deep_getsizeof(k, seen) for k, v in obj.items())
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(deep_getsizeof(i, seen) for i in obj)

    return size


c = 0
while c < 10:
    x = [randint(1,100) for _ in range(1, 101)]
    sleep(1)
    print(f"Deep size: {deep_getsizeof(x)} Bytes")
    c += 1
