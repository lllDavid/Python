import json

def leseJSON(file):
    with open(file,"r") as jsonFile:
        loadedJson = json.load(jsonFile)
        for entry in loadedJson:
            print("Name: ",entry["name"])
            print("Hersteller: ",entry["hersteller"])

    