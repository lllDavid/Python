import json

#Objekte & JSON
#Aufgabe 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def personObjectToJson(list):
        jsonList = []
        for entry in list:
            jsonFormat = {
                "name": entry.name,
                "age": entry.age
            }
            jsonList.append(jsonFormat)
        with open("Aufgabe1Persons.json", "w") as jsonFile:
            json.dump(jsonList, jsonFile)

persons = [Person("David", 27), Person("Daniel", 25), Person("Sammy", 20)]

Person.personObjectToJson(persons)



#Aufgabe 2
with open("Aufgabe1Persons.json", "r") as jsonFile:
    loadedJson = json.load(jsonFile)
    for entry in loadedJson:
        person = Person(entry['name'], entry['age'])
        print("Name:", person.name)
        print("Age:", person.age)



#Aufgabe 3

personen = {}

with open("persons.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(", ")
        personen[name] = int(age)

with open("Aufgabe3Persons.json", "w") as jsonFile:
    json.dump(personen, jsonFile)

print(personen)

 
#Aufgabe 4
class JSON:
    def __init__(self, input, output):
        self.input = input
        self.output = output
    
    def jsonVerarbeitung(self, newData):
            with open(self.input, "r") as jsonFile:
                data = json.load(jsonFile)
            
            data["name"] = newData[0]
            data["age"] = newData[1]

            with open(self.output, "w") as jsonFile:
                json.dump(data, jsonFile)

instanz = JSON("Aufgabe3Persons.json", "Aufgabe4Output.json")
instanz.jsonVerarbeitung(["Karim",23])



#Dynamisches Laden von Dateien
# Aufgabe 5

import importlib 

class Modul:
    def importModul(modulName, modulFunktion, *funktionsParameter):  
        modul = importlib.import_module(modulName) 
        print("Name des Moduls:", modul.__name__) 
        
        funktion = getattr(modul, modulFunktion)
        funktion(*funktionsParameter)
  
Modul.importModul("modul", "addition", 2, 3)



