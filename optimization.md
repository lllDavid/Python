- cdef
- @cython.boundscheck(False) and @cython.wraparound(False)
- built in functions, libraries
- numpy arrays instead of regular lists / generators for large files
- multiprocessing(cpu bound) and multithreading(i/o bound)
- avoid nested loops
- sets when you only care about membership testing
- dictionaries when you need to store and retrieve values
- __slots__ (weakref, )
- __getitem__ ...
- @property (cached computation)
- lru cache

