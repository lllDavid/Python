#1)
def fibonacci(wert):
    a,b=0,1
    
    for _ in range(wert):
        print(a)
        a,b=b,a+b

wert = int(input("Geben sie eine Range an: "))
fibonacci(wert)


#2)
def fibonacci():
    array = []
    a,b=0,1

    for _ in range(10):
        array.append(a)
        a,b=b,a+b
    return array

numbers = fibonacci()
for num in numbers:
    print(num)

fibonacci()