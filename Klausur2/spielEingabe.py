import json

class Eingabe:
   def toJSON():
    data={}
    data['name']=input("Spielname: ")
    data['hersteller']=input("Hersteller: ")
 
    return (data)
out=[]
while True:
    quit=input("Weiter Eingaben ? (Y/N)")
    if quit.lower() == 'n':
        break
    record = Eingabe.toJSON()
    out.append(record)
    with open("lieblingsspiel.json","w") as jsonFile:
       json.dump(out,jsonFile)


