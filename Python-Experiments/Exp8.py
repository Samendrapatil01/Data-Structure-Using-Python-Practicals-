# Experiment 8: Object-Oriented Programming

# Creating a class and object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Samendra", 85)
s1.display()

# Inheritance
class Person:
    def introduce(self):
        print("I am a person.")

class StudentPerson(Person):
    def study(self):
        print("I am studying Python.")

s2 = StudentPerson()
s2.introduce()
s2.study()

# Multiple inheritance
class Father:
    def father_info(self):
        print("This is the father class.")

class Mother:
    def mother_info(self):
        print("This is the mother class.")

class Child(Father, Mother):
    pass

child = Child()
child.father_info()
child.mother_info()

# Method overriding
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

square = Square(5)
print("Area of square:", square.area())
