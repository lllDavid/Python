import json

class DatenEingabe:
    def userInput():
        userInputData = {
            "name": str(input("Name: ")),
            "alter": int(input("Alter: "))
        }
        
        with open("daten.json", "w") as datei:
            json.dump(userInputData, datei)
        
DatenEingabe.userInput()
