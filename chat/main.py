from messages import send_message
from user import register_user

def main():
    username=input("Enter a username:")
    register_user(username)

    message = input("Enter a mesage:")
    send_message(message)

if __name__ == "__main__":
    main()