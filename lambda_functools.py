from functools import lru_cache
cached_abs = lru_cache(maxsize=128)(lambda x: abs(x))


from functools import partial
double = partial(lambda x, y: x * y, 2)


from functools import reduce
sum_squares = lambda nums: reduce(lambda acc, x: acc + x*x, nums, 0)


from functools import cmp_to_key
compare_length = lambda a, b: len(b) - len(a)
key_func = cmp_to_key(compare_length)


from functools import total_ordering
@total_ordering
class Box:
    def __init__(self, volume):
        self.volume = volume
    __eq__ = lambda self, other: self.volume == other.volume
    __lt__ = lambda self, other: self.volume < other.volume