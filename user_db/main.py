from user_db import UserDB
from auth_roles import Role, Permission


def main():
    user_db = UserDB()

    user_db.add_user(1, "David", Role.ADMIN)
    user_db.add_user(2, "Tom", Role.MODERATOR)
    user_db.add_user(3, "Jonas", Role.USER)

    print("\nList of users:")
    user_db.list_users()

    print("\nCheck permissions:")
    print(f"Does Tom have DELETE permission? {user_db.user_has_permission(2, Permission.DELETE)}")  
    print(f"Does David have MANAGE_USERS permission? {user_db.user_has_permission(1, Permission.MANAGE_USERS)}")  

    print("\nGetting user with ID 2:")
    print(user_db.get_user(2))

    user_db.remove_user(2)

    print("\nList of users after removal:")
    user_db.list_users()

    print("\nGetting removed user with ID 2:")
    print(user_db.get_user(2))

main()