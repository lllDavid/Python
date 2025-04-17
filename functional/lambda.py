def multiply(a):
    return lambda b: lambda c: a * b * c

triple_product = multiply(2)(3)
print(triple_product(4)) 
