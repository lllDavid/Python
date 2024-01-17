# Übungen für die erste Kurzarbeit über Klassen/Objekte/Vererbung
# Objekte/Klassen Aufgaben
#1)
class Person:
    def __init__(self,name,alter):
        self.name=name
        self.alter=alter

    def vorstellen(self):
        print(f'"Hallo mein Name ist {self.name} und ich bin {self.alter} Jahre alt!"')

p1=Person("David",26)
p1.vorstellen()

#3)
class Tier:
    art="Katze"
    laut="Miau"

    def machenLaut(self):
        print(self.art,self.laut)

t1=Tier()
t1.machenLaut()

#4,5,(2 von Vererbung))
class Student(Person):
    matrikelnummer=666

    def vorstellen(self):
        print(f'"Hallo mein Name ist {self.name} und ich bin {self.alter} Jahre alt. Meine Matrikelnummer ist {self.matrikelnummer}."')

    def studieren():
        print("Ich studiere gerade...")
s1=Student("David",26)
s1.vorstellen()

#6,7)
class Auto:
    marke="BMW"
    modell="5er"
    __kilometerstand=50000
    
    def standErhoehen(self,zaehler):
        self.__kilometerstand=self.__kilometerstand+zaehler
        print(f'"Neuer Kilometerstand: {self.__kilometerstand}"')

    def standFestlegen(self, kilometerstand):
        self.__kilometerstand = kilometerstand

a1=Auto()
a1.standFestlegen(70000)
a1.standErhoehen(200)


#8)
class Buch:
    titel="Bibel"
    autor="???"
    seitenzahl="666"

    def vorstellen(self):
        print(f'"Das Buch heißt {self.titel} ist vom Autor {self.autor} und hat {self.seitenzahl} Seiten"')

b1=Buch()
b1.vorstellen()

## Vererbung
#1)
class Dozent(Person):
    fachgebiet="Geschichte"

#3)
class Professor(Dozent):
    publikationen=23

    def vorstellen(self):
        super().vorstellen()
        print(f'"Mein Name ist {self.name}, mein Alter ist {self.alter} und meine Publikationen bisher sind {self.publikationen}"')

p1=Professor("David",26)
p1.vorstellen()


#2)
class Doktorand(Student):
    forschungsgebiet="Mathematik"

    def studieren():
        print("Ich forsche gerade")
    
#4)
class Forscher:
    forschungsfeld="Deutsch"

class Schriftsteller:
    veroeffentlichteBuecher=7

class Wissenschaftsautor(Forscher,Schriftsteller):
    def ausgabe(self):
        print(f'"Forschungsfeld: {self.forschungsfeld}, Veröffentlichte Bücher: {self.veroeffentlichteBuecher}"')
        
autor1=Wissenschaftsautor()
autor1.ausgabe()

