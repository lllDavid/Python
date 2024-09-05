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

persons = [Person("David", 27), Person("Maxwell", 25), Person("Tyler", 20)]

Person.personObjectToJson(persons)



#Aufgabe 2
with open("Aufgabe1Persons.json", "r") as jsonFile:
    loadedJson = json.load(jsonFile)
    for entry in loadedJson:
        person = Person(entry['name'], entry['age'])



#Aufgabe3
persons = []
 
with open("persons.txt","r") as txtFile:
    for line in txtFile:
        name,age = line.strip().split(", ")
        persons.append({"name": name, "age": int(age)})
 
with open("Aufgabe3Persons.json","w") as jsonFile:
    json.dump(persons,jsonFile)
   
 
 
#Aufgabe4
#Hinzufügen von Einträgen
class JSON:
    def __init__(self,inputFile,outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
    
    def jsonBearbeiten(self,newData):
        with open(self.inputFile,"r") as jsonFile:
            currentData = json.load(jsonFile)
 
        currentData.append({"name": newData[0], "age": newData[1]})
 
        with open(self.outputFile,"w") as jsonFile:
            json.dump(currentData,jsonFile)
 
ini = JSON("Aufgabe3Persons.json","Aufgabe4Output.json")
ini.jsonBearbeiten(["Alex",30])



#Einträge bearbeiten
import json
 
class JSON:
    def __init__(self,inputFile,outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
   
    def jsonBearbeiten(self,index,key,newValue):
        with open(self.inputFile,"r") as jsonFile:
            currentData = json.load(jsonFile)
 
        currentData[index][key] = newValue
 
        with open(self.outputFile,"w") as jsonFile:
            json.dump(currentData,jsonFile)
 
ini = JSON("Aufgabe3Persons.json","Aufgabe4Output.json")
ini.jsonBearbeiten(1,"name","ChangedTestName")



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



