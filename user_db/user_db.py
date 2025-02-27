from dataclasses import dataclass

@dataclass
class UserDB:
    users_list:list = [] 
    users_dict:dict = {}

class User:
    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Password: {self.password}"
    

user1 = User("David_X","david@company.com","12345678")

user2 = User("David_Y","david@company.com","12345678")

user3 = User("David_Z","david@company.com","12345678")

user_db = UserDB()

user_db.users_list.append(user1)
user_db.users_list.append(user2)
user_db.users_list.append(user3)

user_db.users_dict["User:"] = user1
user_db.users_dict["User:"] = user2
user_db.users_dict["User:"] = user3

print(f"Users in list: {user_db.users_list}")
print(f"Users in dict: {user_db.users_dict}")
