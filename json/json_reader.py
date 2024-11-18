import json

def json_reader(file) -> None:
    with open(file, "r") as json_file:
        file_data = json.load(json_file)
        print(file_data)

