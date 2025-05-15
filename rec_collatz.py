def c(n):
    if n == 1:
        return 
    
    elif n % 2 == 0:
        n = n // 2
        print(n)

    else:
        n = n * 3 + 1
        print(n)

    c(n)

for i in range(1, 10):
    c(i)


def c(n):
    if n == 1:
        return

    if n % 2 == 0:
        print(n // 2)
        c(n // 2)  

    else:
        print(n * 3 + 1)
        c(n * 3 + 1) 

for i in range(1, 10):
    c(i)
