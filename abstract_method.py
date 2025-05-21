from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, species):
        self.name, self.age, self.species = name, age, species

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

    def work(self): print(f"{self.job_title} is working!")
    def take_break(self): print(f"{self.job_title} is taking a break.")

class Human(Animal, WorkerActions):
    def __init__(self, name, age, species, job_title, gender):
        Animal.__init__(self, name, age, species)
        WorkerActions.__init__(self, job_title)
        self.gender = gender

    def speak(self): print(f"{self.name} says: 'Hello, I am a {self.gender} {self.job_title}'")
    def move(self): print(f"{self.name} is walking to the office.")
    def sleep(self, hours): print(f"{self.name} is sleeping for {hours} hours.")
    def eat(self, food): print(f"{self.name} is eating {food}")

class Athlete(Human):
    def __init__(self, *args, sport):
        super().__init__(*args)
        self.sport = sport

    def speak(self): print(f"{self.name} says: 'I am an athlete in {self.sport}'")
    def move(self): print(f"{self.name} is running in a marathon for {self.sport}")
    def train(self): print(f"{self.name} is training hard for {self.sport}")

class Student(Human):
    def __init__(self, *args, school):
        super().__init__(*args)
        self.school = school

    def speak(self): print(f"{self.name} says: 'I am a student at {self.school}'")
    def move(self): print(f"{self.name} is walking to school.")
    def study(self): print(f"{self.name} is studying for exams at {self.school}")

class Robot(Animal, WorkerActions):
    def __init__(self, name, age, species, job_title, model):
        Animal.__init__(self, name, age, species)
        WorkerActions.__init__(self, job_title)
        self.model = model

    def speak(self): print(f"{self.name} says: 'I am a robot model {self.model}'")
    def move(self): print(f"{self.name} is moving with precision.")
    def sleep(self, hours): print(f"{self.name} does not sleep. I am always on standby.")
    def eat(self, food): print(f"{self.name} does not eat organic food. I am powered by electricity.")
    def repair(self): print(f"{self.name} is being repaired.")

class Car:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model
    def drive(self): print(f"The {self.brand} {self.model} is driving.")

class HumanWithCar(Human):
    def __init__(self, *args, car):
        super().__init__(*args)
        self.car = car
    def drive_car(self): self.car.drive()

p1 = Human("David", 30, "Human", "Engineer", "Male")
p1.speak(); p1.move(); p1.eat("Pizza"); p1.sleep(8); p1.work(); p1.take_break()

athlete = Athlete("John", 25, "Human", "Professional Runner", "Male", sport="Running")
athlete.speak(); athlete.move(); athlete.train()

student = Student("Anna", 20, "Human", "Student", "Female", school="Harvard University")
student.speak(); student.move(); student.study()

robot = Robot("RoboX", 5, "Robot", "Assistant", "RX-5000")
robot.speak(); robot.move(); robot.sleep(0); robot.eat("Electricity"); robot.repair()

car = Car("Tesla", "Model S")
human_with_car = HumanWithCar("Mark", 28, "Human", "Driver", "Male", car=car)
human_with_car.speak(); human_with_car.move(); human_with_car.drive_car()
