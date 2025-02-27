from dataclasses import dataclass, field
from typing import Optional

# Base class for Human with more complex behavior
@dataclass
class Human:
    name: str
    age: int
    birthyear: int
    height: float  # Height in feet
    weight: float  # Weight in pounds
    gender: Optional[str] = field(default="Not Specified")
    nationality: Optional[str] = field(default="Not Specified")
    occupation: Optional[str] = field(default="Unemployed")
    
    # Method to calculate BMI (Body Mass Index)
    def calculate_bmi(self) -> float:
        # BMI = weight (lbs) / height (inches)^2 * 703
        height_in_inches = self.height * 12
        bmi = (self.weight / (height_in_inches ** 2)) * 703
        return round(bmi, 2)

    # Method to categorize the BMI
    def bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    @classmethod
    def from_birthyear(cls, name: str, birthyear: int, height: float, weight: float, gender: Optional[str] = None, nationality: Optional[str] = None, occupation: Optional[str] = None):
        current_year = 2025
        age = current_year - birthyear
        return cls(name, age, birthyear, height, weight, gender, nationality, occupation)

    # Method to update the human's weight
    def update_weight(self, new_weight: float):
        print(f"Updating {self.name}'s weight from {self.weight} lbs to {new_weight} lbs.")
        self.weight = new_weight

    # Method to update the human's height
    def update_height(self, new_height: float):
        print(f"Updating {self.name}'s height from {self.height} ft to {new_height} ft.")
        self.height = new_height

    # Method to display a summary of the human's data
    def display_info(self):
        bmi = self.calculate_bmi()
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Birth Year: {self.birthyear}")
        print(f"Height: {self.height} feet")
        print(f"Weight: {self.weight} lbs")
        print(f"Gender: {self.gender}")
        print(f"Nationality: {self.nationality}")
        print(f"Occupation: {self.occupation}")
        print(f"BMI: {bmi}")
        print(f"BMI Category: {self.bmi_category()}")


# Child class: Employee (inherits from Human and adds more attributes related to employment)
@dataclass
class Employee(Human):
    employee_id: str
    department: str
    salary: float
    
    def give_raise(self, raise_percentage: float):
        raise_amount = (self.salary * raise_percentage) / 100
        self.salary += raise_amount
        print(f"{self.name}'s salary has been increased by {raise_percentage}%. New salary: ${self.salary:.2f}")

    def change_department(self, new_department: str):
        print(f"{self.name} has transferred to the {new_department} department.")
        self.department = new_department

    def display_employee_info(self):
        self.display_info()  # From the Human class
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:.2f}")


# Child class: Student (inherits from Human and adds more attributes related to studies)
@dataclass
class Student(Human):
    student_id: str
    major: str
    gpa: float
    
    def study(self, hours: int):
        print(f"{self.name} is studying for {hours} hours.")

    def update_gpa(self, new_gpa: float):
        print(f"Updating {self.name}'s GPA from {self.gpa} to {new_gpa}.")
        self.gpa = new_gpa

    def display_student_info(self):
        self.display_info()  # From the Human class
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa}")


# Creating a Human object using the from_birthyear class method
alice = Human.from_birthyear(name="Alice", birthyear=1990, height=5.7, weight=140, gender="Female", nationality="American", occupation="Engineer")
alice.display_info()
print()

# Updating Alice's weight and height
alice.update_weight(150)
alice.update_height(5.8)
alice.display_info()
print()

# Creating an Employee object
emp = Employee.from_birthyear(name="Bob", birthyear=1985, height=6.0, weight=180, gender="Male", nationality="Canadian", occupation="Manager", employee_id="E1234", department="Sales", salary=75000)
emp.display_employee_info()
emp.give_raise(5)
emp.change_department("Marketing")
emp.display_employee_info()
print()

# Creating a Student object
stu = Student.from_birthyear(name="Charlie", birthyear=2000, height=5.9, weight=160, gender="Male", nationality="British", occupation="Student", student_id="S5678", major="Computer Science", gpa=3.8)
stu.display_student_info()
stu.study(4)
stu.update_gpa(4.0)
stu.display_student_info()
