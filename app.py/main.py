class UserDB:
    users = {}

class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __str__(self):
        return f"ID: {self.id} Username: {self.username}"

class UserManager():
    def add_single_user(self, user:User):
        UserDB.users[user.id] = user.username
        print(f"User {user.username} added to DB")

    def add_multiple_users(self, users:list):
        for i in users:
            for k,v in i.items():
                UserDB.users[k] = v
            print(f"User: {v} added to DB")

    def show_users(self):
        for k,v in UserDB.users.items():
            print(f"ID: {k} Username: {v}")


um = UserManager()

# Single
user = User(0,"Mark")
print(user)
um.add_single_user(user)

# Multiple
list_users = [{1:"David"}, {2:"Tom"}, {3:"Alice"}]
um.add_multiple_users(list_users)

print(UserDB.users)

