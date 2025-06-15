def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)

result = closure(5)
print(result)  

# Creates a counter with increment, decrement that keep count private.
def secure_counter():
    count = 0 

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        if count > 0:
            count -= 1
        return count

    def get_count():
        return count

    return increment, decrement, get_count

inc, dec, current = secure_counter()

print(inc())    
print(inc())    
print(dec())    
print(current()) 

