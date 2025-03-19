import timeit

def old():
    result = []
    for i in range(10):
        row = []
        for j in range(10):
            num = i * j  
            if num % 2 == 0: 
                row.append(num ** 2)  
        result.append(row)
    total_sum = sum(sum(row) for row in result)
    return total_sum

def new():
    result = [
        [num ** 2 for num in range(10) if (i * num) % 2 == 0]  
        for i in range(10)
    ]
    total_sum = sum(sum(row) for row in result)
    return total_sum

old_time = timeit.timeit(old, number=10000)
new_time = timeit.timeit(new, number=10000)

print(f"Old function time: {old_time}")
print(f"New function time: {new_time}")
