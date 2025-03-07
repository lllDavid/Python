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




