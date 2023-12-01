# 1. PYTHON-KLAUSUR

# Gib zurerst Deinen Namen unten ein und speichere die Datei als "klausur_python_vorname_nachname.py ab". Schreibe die Ergebnisse direkt unterhalb der Aufgaben. Achte auf die Punkteverteilung.

# Name: David Wagner
#=====================================================================================================================

# Aufgabe 1: Iteriere über eine Liste von Obstsorten und gib jedes Element aus. 5 Punkte

obst = ["Banane","Apfel","Birne"]
for o in obst:
    print(o)

# Aufgabe 2: Schreibe eine Funktion, die einen Iterator für die Fibonacci-Folge erstellt und gib die ersten 20 Zahlen aus. 10 Punkte

def fibonacci():
    a,b=0,1
    array = []
    for _ in range(20):
        array.append(a)
        a,b=b,a+b
    return array

numbers = fibonacci()
for n in numbers:
    print(n)

# Aufgabe 3: Gib jeden Buchstaben eines Wortes rückwärts aus. 5 Punkte

wort = "Testwort"
reversedWort = reversed(wort)
for i in reversedWort:
    print(i)

# Aufgabe 4: Erstelle eine Klasse, die einen Iterator für die Quadrate von Zahlen von 1 bis 10 erstellt. 15 Punkte

class myIter:
    def __iter__(self):
        self.counter = 1
        return self
    def __next__(self):
        if self.counter <=10:
            quad = self.counter**2
            self.counter+=1
            return quad
        raise StopIteration

numbers = myIter()
for n in numbers:
    print(n)

# Aufgabe 5: Schreibe eine Funktion, die nur die geraden Zahlen aus einer Liste ausgibt. 10 Punkte

zahlen = [1,2,3,4,5,6,7,8,9,10]

for z in zahlen:
    if z % 2 == 0:
        print(z)

# Aufgabe 6: Erstelle ein Modul namens 'meinmodul' mit einer Funktion 'begruessung', die einen Namen als Parameter nimmt und eine Begrüßung ausgibt. 5 Punkte 

# Aufgabe 7: Importiere dein Modul 'meinmodul' in dieses Skript und rufe die Funktion 'begruessung' mit deinem Namen auf. 5 Punkte

import meinmodul as mm
mm.begruessung("David")

# Aufgabe 8: Füge dem Modul 'meinmodul' ein Dictionary 'person1' hinzu mit den Schlüsseln 'name', 'alter', und 'stadt'. 5 Punkte

# Aufgabe 9: Importiere das Dictionary 'person1' aus deinem Modul und gib das Alter der Person aus. 5 Punkte

from meinmodul import person1
print(person1["alter"])

# Aufgabe 10: Erstelle einen Alias 'mm' für dein Modul 'meinmodul' und greife auf die Stadt der 'person1' aus dem Modul zu. 5 Punkte

import meinmodul as mm
x = mm.person1["stadt"]
print(x)

# Aufgabe 11: Erstelle eine Basisklasse mit dem Namen 'Tier' mit den Attributen 'name' und 'fellfarbe' und einer Methode 'futter', die "Ich liebe Knochen" ausgibt. 5 Punkte

class Tier:
    name="Bello"
    fellfarbe="Grau"

    def futter(self):
        print("Ich liebe Knochen")

t1=Tier()
t1.futter()

# Aufgabe 12: Leite eine Klasse 'Hund' von der Klasse 'Tier' ab und fügen eine Methode 'anzeige' hinzu, die Name und Fellfarbe des Hundes ausgibt. 5 Punkte

class Hund(Tier):
    def anzeige(self):
        print(f'Name: {self.name} und Fellfarbe: {self.fellfarbe}')

h1 = Hund()
h1.anzeige()

# Aufgabe 13: Erstelle ein Objekt der Klasse 'Hund', setze seinen Namen auf 'Fussel' und rufe die Methode 'anzeige' auf. 5 Punkte

h2 = Hund()
h2.name = "Fussel"
h2.anzeige()

# Aufgabe 14: Rufe die Methode 'futter' für das Objekt der Klasse 'Hund' auf. 5 Punkte

h2.futter()

# Aufgabe 15: Erstelle eine Klasse 'Polygon' mit einem Konstruktor, der die Anzahl der Seiten in einem Argument erhalten kann und eine Methode 'eingabeSeiten', die die Längen der Seiten bei Eingabe über die Konsole einliest. 10 Punkte

class polygon:
    def __init__(self,anzahl):
        self.a = anzahl
      
    def input(self):
        self.seiten = [float(input("Länge der " +str(i+1) +" Seite: ")) for i in range(self.a)]

    def output(self):
        for i in range(self.a):
            print("Seite",i+1,"ist",self.seiten[i])

p = polygon(3)
p.input()
p.output()

   




