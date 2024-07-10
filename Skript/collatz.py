def collatz(number):
    count = 1
    while number != 1:
        print(f"Zwischenschritt {count}: {number}")
        number = number // 2 if number % 2 == 0 else number * 3 + 1
        count += 1
    print(f"Zwischenschritt {count}: {number}") 
    if number == 1:
        print("Zahl 1 erreicht!")
    return count

for i in range(1, 20):
    print("\n")
    print(f"Zahl: {i}")
    collatz(i)
   
