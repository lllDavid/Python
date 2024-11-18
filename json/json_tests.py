import json
import importlib 

# Aufgabe 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_object_to_json(self, list):
        json_list = []
        for entry in list:
            json_format = {
                "name": entry.name,
                "age": entry.age
            }
            json_list.append(json_format)
        with open("persons.json", "w") as json_file:
            json.dump(json_list, json_file)

person = Person("Mark", 23)
person.person_object_to_json(person)

# Aufgabe 2
with open("persons.json", "r") as json_file:
    json_data = json.load(json_file)
    for entry in json_data:
        person = Person(entry['name'], entry['age'])

# Aufgabe 3
persons = []
 
with open("persons.txt","r") as txt_file:
    for line in txt_file:
        name,age = line.strip().split(", ")
        persons.append({"name": name, "age": int(age)})
 
with open("persons2.json","w") as json_file:
    json.dump(persons, json_file)

# Aufgabe 4
class JSON1:
    def __init__(self,input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    
    def process_json(self,newData):
        with open(self.input_file,"r") as json_file:
            current_data = json.load(json_file)
 
        current_data.append({"name": newData[0], "age": newData[1]})
 
        with open(self.output_file,"w") as json_file:
            json.dump(current_data, json_file)
 
j1 = JSON1("persons2.json","persons3.json")
j1.process_json(["Alex", 30])

class JSON2:
    def __init__(self,input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
   
    def process_json(self, index, key, new_value):
        with open(self.input_file,"r") as json_file:
            current_data = json.load(json_file)
 
        current_data[index][key] = new_value
 
        with open(self.output_file,"w") as json_file:
            json.dump(current_data,json_file)
 
j2 = JSON2("persons2.json","persons3.json")
j2.process_json(1,"name", "Changed name")

# Aufgabe 5
class Module:
    def import_module(self, module_name, modul_function, *function_parameters):  
        my_module = importlib.import_module(module_name) 
        print("Name: ", my_module.__name__) 
        
        my_function = getattr(my_module, modul_function)
        my_function(*function_parameters)

m = Module()
m.import_module("my_module", "add", 2, 3)




