from enum import Enum

class Roles(Enum):
    USER = "User"
    ADMIN = "Admin"

class User:
    def __init__(self, rights:Roles):
        self.rights = rights

    def get_rights(self):
        return self.rights

user = User(Roles.USER)
print(user.get_rights())
