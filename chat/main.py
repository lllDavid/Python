from messages import send_message
from user import register_user

def generate_response(user_message):
    '''
    import openai

    openai.api_key = 'YOUR_API_KEY'

    def generate_response(user_message):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    '''
    return f"Bot: I received your message '{user_message}'. How can I assist you further?"

def main():
    username = input("Enter a username: ")
    try:
        register_user(username)
    except Exception as e:
        print(f"Error registering user: {e}")
        return

    print(f"Welcome {username}! Start chatting (type 'quit' to exit):")

    while True:
        message = input(f"{username}: ")
        if message.lower() == 'quit':
            print("Exiting chat...")
            break
            
        send_message(username, message)  

        bot_response = generate_response(message)
        send_message("bot", bot_response)
        print(bot_response)

if __name__ == "__main__":
    main()
