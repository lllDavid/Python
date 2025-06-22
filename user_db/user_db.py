from typing import List, Dict, Optional
from dataclasses import dataclass, field

from auth_roles import Role, Permission, has_permission


@dataclass
class UserDB:
    users_list: List[dict] = field(default_factory=list)
    users_dict: Dict[int, dict] = field(default_factory=dict)

    def add_user(self, user_id: int, user_name: str, role: Role = Role.USER):
        user = {"id": user_id, "name": user_name, "role": role}
        self.users_list.append(user)
        self.users_dict[user_id] = user
        print(f"User '{user_name}' added with role '{role.name}'.")

    def remove_user(self, user_id: int):
        if user_id in self.users_dict:
            user = self.users_dict.pop(user_id)
            self.users_list = [u for u in self.users_list if u["id"] != user_id]
            print(f"User '{user['name']}' removed.")
        else:
            print("User not found!")

    def get_user(self, user_id: int) -> Optional[dict]:
        return self.users_dict.get(user_id, None)

    def list_users(self):
        if not self.users_list:
            print("No users available.")
        for user in self.users_list:
            print(f"ID: {user['id']}, Name: {user['name']}, Role: {user['role'].name}")

    def user_has_permission(self, user_id: int, permission: Permission) -> bool:
        user = self.get_user(user_id)
        if not user:
            print("User not found!")
            return False
        role = user["role"]
        return has_permission(role, permission)