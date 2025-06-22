import json

def user_input() -> None:
    user_data = {
        "name": str(input("Name: ")),
        "age": int(input("Age: "))
    }
    
    with open("data.json", "w") as file:
        json.dump(user_data, file)

def json_reader(file) -> None:
    with open(file, "r") as json_file:
        file_data = json.load(json_file)
        print(file_data)

json_reader("data.json")