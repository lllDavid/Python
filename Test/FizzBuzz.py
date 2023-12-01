#1)
for i in range(1,101):

    if i%15 == 0:
        print("FizzBuzz")
                                               
    elif i%5 == 0:
        print("Buzz")

    elif i%3 == 0:
        print("Fizz")

    else:
        print(i)

#2)
fizzbuzz = lambda x: "Fizz"*(x % 3 == 0) + "Buzz"*(x % 5 == 0) or x        
result = [fizzbuzz(x) for x in range(1, 101)]
print(result)


#3)
for i in range(100):print(i%3//2*"Fizz"+i%5//4*"Buzz"or-~i)          