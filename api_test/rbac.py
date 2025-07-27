from enum import Enum
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"

users = {
    "alice": {"username": "alice", "role": UserRole.admin},
    "bob": {"username": "bob", "role": UserRole.user},
    "eve": {"username": "eve", "role": UserRole.guest},
}

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = users.get(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user

def role_required(required_role: UserRole):
    def role_checker(user=Depends(get_current_user)):
        if user["role"] != required_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
        return user
    return role_checker

@app.get("/admin-data")
def read_admin_data(user=Depends(role_required(UserRole.admin))):
    return {"msg": f"Hello Admin {user['username']}, here is your secret data."}

@app.get("/user-data")
def read_user_data(user=Depends(role_required(UserRole.user))):
    return {"msg": f"Hello User {user['username']}, here is your user data."}

@app.get("/guest-data")
def read_guest_data(user=Depends(role_required(UserRole.guest))):
    return {"msg": f"Hello Guest {user['username']}, limited access granted."}