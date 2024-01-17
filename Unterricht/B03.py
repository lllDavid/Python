#Iteratoren
#Aufgabe1

obst=["Banane","Birne","Apfel"]
for o in obst:
    print(o)



#Aufgabe2

def fibonacci():
    array=[]
    a,b=0,1
    
    for _ in range(10):
        array.append(a)                  
        a,b=b,a+b
    return array

zahlen = fibonacci()
for i in zahlen:
    print(i)


def fibonacci(wert):
    a,b=0,1
    
    for _ in range(wert):
        print(a)
        a,b=b,a+b
fibonacci(int(input("Wie oft soll ausgegeben werden ?")))



#Aufgabe3

wort = "Hallo"
umgekehrtesWort=reversed(wort)
for i in umgekehrtesWort:
    print(i)



#Aufgabe4

class meinIterator:
    def __init__(self):
        self.zahl=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.zahl<=10:
            quadrat=self.zahl**2
            self.zahl+=1
            return quadrat
        raise StopIteration
        
quadrate = meinIterator()
for quadrat in quadrate:
    print(quadrat)



#Aufgabe5

zahlen=[1,2,3,4,5,6,7,8,9,10]

def geradeZahlen():
    for i in zahlen:
        if i%2==0:
            print(i)
        else:
            print(" ")
geradeZahlen()


#Fehlerbehandlung
#Aufgabe1 

try:
    zahl1= int(input("Geben sie die erste Zahl ein: "))
    zahl2 = int(input("Geben sie die zweite Zahl ein: "))
    operator = input("Wählen sie den Operator aus: +,-,/,*")
    match(operator):
        case "+":
            ergebnis=zahl1+zahl2
       
        case "-":
            ergebnis=zahl1-zahl2
     
        case "/":
            ergebnis=zahl1/zahl2
      
        case "*":
            ergebnis=zahl1*zahl2

    print(ergebnis)
       
except ValueError:
   print("Ganzzahl eingeben")

except ZeroDivisionError:
   
    print("Zahl ist 0")



#Aufgabe2

def function():
    try:
        zeichenkette = input("Geben sie einen String ein: ")
        umgewandelteZeichenkette = int(zeichenkette)
        print (umgewandelteZeichenkette)
    except ValueError:
        print("Keine gültige Ganzzahl!")
function()



#Aufgabe3

try:
    liste = ["Test","Beispiel",97]
    eingabe=int(input("Wählen sie den Index: 0,1 oder 2: "))
    print(liste[eingabe])
 

except IndexError:
    print("Index out of Range")



#Aufgabe4

try:
    zahl1=int(input("Zahl1: "))
    zahl2=int(input("Zahl2: "))
    ergebnis = zahl1/zahl2
    print(f'Das Ergebnis ist {ergebnis}')
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("Value Error")
except Exception as e:
    print(f'Der Fehler ist {e}')


#String-Formatierung
#Aufgabe1

name = input("Namen eingeben: ")
alter = int(input("Alter eingeben: "))
ausgabe="Mein Name ist {0} und mein Alter ist {1}"

print(ausgabe.format(name,alter))



#Aufgabe2 

vorname = input("Vornamen eingeben: ")
print(f'Hallo, {vorname}! Wie gehts dir heute ?')