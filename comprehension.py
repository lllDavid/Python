import timeit

# Old function using traditional for loops
def old():
    result = []
    for i in range(10):
        row = []
        for j in range(10):
            num = i * j  # Some operation on the indices
            if num % 2 == 0:  # Filter: keep only even numbers
                row.append(num ** 2)  # Apply transformation: square the even numbers
        result.append(row)
    # Do some further operation on the matrix (e.g., sum all elements)
    total_sum = sum(sum(row) for row in result)
    return total_sum

# New function using list comprehension
def new():
    result = [
        [num ** 2 for num in range(10) if (i * num) % 2 == 0]  # Nested comprehension with conditions and transformation
        for i in range(10)
    ]
    total_sum = sum(sum(row) for row in result)
    return total_sum

# Time the old and new functions
old_time = timeit.timeit(old, number=10000)
new_time = timeit.timeit(new, number=10000)

# Print results
print(f"Old function time: {old_time}")
print(f"New function time: {new_time}")
