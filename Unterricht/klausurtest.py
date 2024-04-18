import json

#Aufgabe 1
class Person:
    def __init__(self,name,alter):
        self.name = name
        self.alter = alter

    def objectTOJson(liste:list):
        json_str = json.dumps(liste)
        print("JSON: ", json_str)

    
p1 = Person("Daniel",34)
p2 = Person("David",12)
p3 = Person("Sammy",89)


personen = []
personen.append(p1)
personen.append(p2)
personen.append(p3)


Person.objectTOJson(personen)



