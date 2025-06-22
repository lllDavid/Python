from enum import Enum, auto

class Role(Enum):
    ADMIN = auto()
    MODERATOR = auto()
    USER = auto()
    GUEST = auto()

class Permission(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    UPDATE = auto()
    MANAGE_USERS = auto()

ROLE_PERMISSIONS = {
    Role.ADMIN: {Permission.READ, Permission.WRITE, Permission.DELETE, Permission.UPDATE, Permission.MANAGE_USERS},
    Role.MODERATOR: {Permission.READ, Permission.WRITE, Permission.UPDATE},
    Role.USER: {Permission.READ, Permission.WRITE},
    Role.GUEST: {Permission.READ},
}

def has_permission(role: Role, permission: Permission) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())

if __name__ == "__main__":
    role = Role.MODERATOR
    print(f"Moderator can delete? {has_permission(role, Permission.DELETE)}")  
    print(f"Moderator can update? {has_permission(role, Permission.UPDATE)}")  