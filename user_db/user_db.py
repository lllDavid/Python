from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class UserDB:
    users_list: List[dict] = field(default_factory=list)
    users_dict: Dict[int, dict] = field(default_factory=dict)

    def add_user(self, user_id: int, user_name: str):
        """Add a user to both users_list and users_dict."""
        user = {"id": user_id, "name": user_name}
        self.users_list.append(user)
        self.users_dict[user_id] = user
        print(f"User '{user_name}' added.")

    def remove_user(self, user_id: int):
        """Remove a user from both users_list and users_dict by user ID."""
        if user_id in self.users_dict:
            user = self.users_dict.pop(user_id)
            self.users_list = [u for u in self.users_list if u["id"] != user_id]
            print(f"User '{user['name']}' removed.")
        else:
            print("User not found!")

    def get_user(self, user_id: int):
        """Retrieve a user by ID from users_dict."""
        user = self.users_dict.get(user_id)
        if user:
            return user
        else:
            return "User not found!"

    def list_users(self):
        """List all users."""
        if not self.users_list:
            print("No users available.")
        for user in self.users_list:
            print(f"ID: {user['id']}, Name: {user['name']}")

user_db = UserDB()

user_db.add_user(1, "David")
user_db.add_user(2, "Tom")
user_db.add_user(3, "Alice")

print("\nList of users:")
user_db.list_users()

print("\nGetting user with ID 2:")
print(user_db.get_user(2))

user_db.remove_user(2)

print("\nList of users after removal:")
user_db.list_users()

print("\nGetting removed user with ID 2:")
print(user_db.get_user(2))
