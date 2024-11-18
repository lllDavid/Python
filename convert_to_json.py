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
            eingabe = input("Weiter? Ja (Taste drücken) Nein (Nein eingeben): ")
            if eingabe == "Nein":
                break

    def save_json(self, filename='data.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.liste, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")

class DatenAusgabe(Daten):
    def print_json(self):
        for entry in self.liste:
            print(json.dumps(entry))

y = DatenAusgabe()
y.save_json()
y.print_json()
