import jwt
import datetime

SECRET_KEY = "123456"

def generate(user_id):
    payload = {
        'user_id': user_id,
        'username': "User",
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=1), 
        'iat': datetime.datetime.now(datetime.UTC)  
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return token

def decode(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"

user_id = 123 

token = generate(user_id)
print(f"Generated JWT: {token}")

decoded_data = decode(token)
print(f"Decoded Payload: {decoded_data}")