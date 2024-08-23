import json

class Daten:
    def __init__(self):
        self.liste = [] 
        while True:
            entry = {
                "name": input("Namen eingeben: "),
                "beruf": input("Beruf eingeben: "),
                "e-mail": input("E-Mail eingeben: ")
            }
            self.liste.append(entry)  
            eingabe = input("Weitere Daten eingeben? Ja (Taste drücken) Nein (Nein eingeben): ")
            if eingabe == "Nein":
                break

class DatenAusgabe(Daten):
    def print_json(self):
        for entry in self.liste:
            print(json.dumps(entry))

y = DatenAusgabe()
y.print_json()