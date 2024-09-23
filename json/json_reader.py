import json

def jsonReader(file):
    with open(file, "r") as jsonFile:
        data = json.load(jsonFile)
        print(data)

