class User:
    def __init__(self, username, password, account_age):
        self.username = username
        self.password = password
        self.account_age = account_age

    def __str__(self):
        return f"User: {self.username}, password: {self.password}, account_age: {self.account_age}"


class UserDB:
    users = {}
    
    def add_user(self, user):
        # Use the username as the key
        self.users[user.username] = user
        print(f"User: {user.username} added")
    
    def get_user(self, username):
        if username in self.users:
            print(f"User {username} found in DB")
            return self.users[username]  # Return the user object
        else:
            print("User not found in DB")
            return None

