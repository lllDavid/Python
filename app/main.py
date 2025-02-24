from user_db import User, UserDB

user = User("David", "123456", 2)
user2 = User("Tom","123211",4)

user_db = UserDB()

user_db.add_user(user)
user_db.get_user("David")

user_db.add_user(user2)
user_db.get_user("Tom")

for k,v in user_db.users.items():
    print(k, v)

