def rec_collatz(n):
    if n == 1:
        return
    
    elif n % 2 == 0:
        n = n //2
        print(n) 
    else:
        n = n * 3 + 1
        print(n)

    rec_collatz(n)

print(rec_collatz(3))


class User2:
    def __init__(self, username, email, password, birthyear, age):
        self.username = username
        self.email = email
        self.password = password
        self.birthyear = birthyear
        self.age = age

    def __str__(self):
        return f"User: {self.username}, {self.email}, {self.password}, {self.birthyear} "
    
    @classmethod
    def greet(cls, username, email, password, birthyear):
        current_year =  2025
        age = 2025-birthyear
        return cls(username, age, email, password, birthyear)

user = User2.greet("David","david@gmail.com",123456,1999)
print(user)


