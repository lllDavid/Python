import secrets

def newToken():
    token = secrets.token_hex(20)
    print(token)

newToken()