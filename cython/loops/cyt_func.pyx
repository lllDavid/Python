def c_function(int x):
    cdef int i, result = 0
    for i in range(x):
        result += i
    return result
