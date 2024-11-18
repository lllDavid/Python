import json

def user_input() -> None:
    user_data = {
        "name": str(input("Name: ")),
        "age": int(input("Age: "))
    }
    
    with open("data.json", "w") as file:
        json.dump(user_data, file)

