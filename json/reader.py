import json
import os

def json_reader(file) -> None:
    if not os.path.exists(file):
        print(f"{file} does not exist.")
        return
    with open(file, "r") as json_file:
        try:
            file_data = json.load(json_file)
            print(file_data)
        except json.JSONDecodeError:
            print("Error reading JSON data.")

if __name__ == "__main__":
    json_reader("data.json")