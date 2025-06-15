from enum import Enum, auto

class Roles(Enum):
    USER = auto()
    MODERATOR = auto()
    ADMIN = auto()

class Permissions(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    BAN_USER = auto()

ROLE_PERMISSIONS = {
    Roles.USER: {Permissions.READ},
    Roles.MODERATOR: {Permissions.READ, Permissions.WRITE, Permissions.BAN_USER},
    Roles.ADMIN: {Permissions.READ, Permissions.WRITE, Permissions.DELETE, Permissions.BAN_USER},
}

class User:
    def __init__(self, username: str, role: Roles):
        self.username = username
        self.role = role
        self.permissions = ROLE_PERMISSIONS[role]
    
    def can(self, permission: Permissions):
        return permission in self.permissions
    
    def get_role(self):
        return self.role.name
    
    def __str__(self):
        perms = ', '.join(p.name for p in self.permissions)
        return f"User: {self.username}, Role: {self.get_role()}, Permissions: {perms}"

alice = User("alice", Roles.USER)
bob = User("bob", Roles.MODERATOR)
carol = User("carol", Roles.ADMIN)

print(alice)
print(f"Can Alice delete? {alice.can(Permissions.DELETE)}")

print(bob)
print(f"Can Bob ban users? {bob.can(Permissions.BAN_USER)}")

print(carol)
print(f"Can Carol write? {carol.can(Permissions.WRITE)}")
