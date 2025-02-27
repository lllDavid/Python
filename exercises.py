def sum_input():
    total = 0
    user_input = ""
    while user_input != "quit":
        user_input = input("Numbers: ")
        if user_input == "quit":
            print("Quiting...")
        else:
            total = total + int(user_input)
            print(f"Sum: {total}")
# sum_input()

def validate_password(password):
    if len(password) >= 8 and any(char in "$#@" for char in password):
        print("Valid password")
        return True
    else:
        print("Invalid password")
        return False
    
# validate_password(input("Enter password: "))

def iterate_dict(article):
    fruits = {"Apple":0.50, "Banana":0.70, "Strawberry":0.20}
    for value in fruits:
        if article == value:
            print(f"Artikel in Liste, Preis: {fruits[value]}")
            break
        else:
            print("Artikel nicht in Liste")
            break

# iterate_dict("Apple")

def questions():
    points = 0
    questions = {"Whats 1+1?":"2", "What does HTML stand for?":"Hyper Text Markup Language", "What does RGB stand for?":"Red Green Blue"}
    for q in questions:
        print("Frage:", q)
        user = input("Antwort: ")
        if user == questions[q]:
            print("Correct")
            points += 1
        else:
            print(f"Wrong. Correct answer: {questions[q]}")

    print(f"Your points: {points}")

# questions()

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*",end=" ")
    print()

def nums():
    nums = [1,5,8,3]
    if 3 in nums:
        return True
    return False

# print(nums())

def isEven(n):
    if n % 2 == 0:
        print(f"{n} Is even")
    else:
        print(f"{n} Is not even")

# isEven(int(input("Enter number: ")))

list = [1,2,3,4,5]
div_list = [i / 2 for i in list]
# print(div_list)

# Binary Search

numbers = [1,2,3]
target = 3

def search(n,t):
    start = 0
    end = len(n) - 1
    while start <= end:
        mid = (start+end)//2
        if n[mid] == t:
            return mid
        elif n[mid] > t:
            end = mid - 1
        elif n[mid] < t:
            start = mid + 1


# print(search(numbers,target))

numbernumbers = [1,2,3,4,5,6,7,8]
targ = 11

def two(nums, t):
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == t:
                return [i,j]
            j += 1
        i += 1

print(two(numbernumbers, targ))

