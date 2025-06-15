from random import randint

x = [{f"Employee_{i}":f"ID_{randint(1,101)}"} for i in range(1,11)]

y = {k: v for d in x for k, v in d.items()}

print(y)
print(y.get("Employee_2", "Not in Dict"))
print(y.get("Employee_20", "Not in Dict"))


from timeit import timeit

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

old_time = timeit(old, number=10000)
new_time = timeit(new, number=10000)

print(f"Old function time: {old_time}")
print(f"New function time: {new_time}")