import timeit

def old():
    result = []
    for i in range(10):
        result.append(i + 1)

def new():
    result = [i + 1 for i in range(10)]

old_time = timeit.timeit(old, number=10000)  
new_time = timeit.timeit(new, number=10000)

print(f"Old function time: {old_time}")
print(f"New function time: {new_time}")
