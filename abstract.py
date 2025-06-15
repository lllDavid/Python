from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    @abstractmethod
    def speak(self): pass

    @abstractmethod
    def move(self): pass

    @abstractmethod
    def sleep(self, hours): pass

    @abstractmethod
    def eat(self, food): pass

    def display_info(self):
        print(f"{self.species} Info: Name: {self.name}, Age: {self.age}")

class WorkerActions:
    def __init__(self, job_title):
        self.job_title = job_title

    def work(self):
        print(f"{self.job_title} is working!")

    def take_break(self):
        print(f"{self.job_title} is taking a break.")

class Human(Entity, WorkerActions):
    def __init__(self, name, age, species, job_title, gender):
        Entity.__init__(self, name, age, species)
        WorkerActions.__init__(self, job_title)
        self.gender = gender

    def speak(self):
        print(f"{self.name} says: 'Hello, I am a {self.gender} {self.job_title}'")

    def move(self):
        print(f"{self.name} is walking to the office.")

    def sleep(self, hours):
        print(f"{self.name} is sleeping for {hours} hours.")

    def eat(self, food):
        print(f"{self.name} is eating {food}")

class Student(Human):
    def __init__(self, *args, school):
        super().__init__(*args)
        self.school = school

    def speak(self):
        print(f"{self.name} says: 'I am a student at {self.school}'")

    def move(self):
        print(f"{self.name} is walking to school.")

    def study(self):
        print(f"{self.name} is studying for exams at {self.school}")

p1 = Human("Leon", 30, "Human", "Engineer", "Male")
p1.speak(); p1.move(); p1.eat("Pizza"); p1.sleep(8); p1.work(); p1.take_break()

student = Student("Anna", 20, "Human", "Student", "Female", school="Harvard University")
student.speak(); student.move(); student.study()
