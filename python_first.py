# working with this concepts
# Attributes

# Inheritance

# Composition

# Aggregation

# Methods

# Polymorphism

# super()

# Abstraction


# ================================
# 1. ATTRIBUTES
# ================================

# Example 1 – Instance Attribute
class Student:
    def __init__(self, name):  # constructor to initialize object
        self.name = name       # instance attribute

s = Student("Ali")             # create object
print(s.name)                  # access attribute


# Example 2 – Multiple Instance Attributes
class Car:
    def __init__(self, brand, year):  # constructor
        self.brand = brand            # instance attribute
        self.year = year              # instance attribute

c = Car("Toyota", 2022)
print(c.brand, c.year)


# Example 3 – Class Attribute
class Animal:
    species = "Mammal"  # class attribute shared by all objects

a1 = Animal()
a2 = Animal()

print(a1.species, a2.species)


# Example 4 – Modifying Attributes
class Person:
    def __init__(self, age):
        self.age = age  # instance attribute

p = Person(20)

p.age = 25  # modify attribute value
print(p.age)


# Example 5 – Dynamic Attribute
class Laptop:
    pass  # empty class

l = Laptop()

l.brand = "Dell"  # dynamically adding attribute
print(l.brand)


# ================================
# 2. INHERITANCE
# ================================

# Example 1 – Basic Inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):  # Dog inherits from Animal
    pass

d = Dog()
d.speak()  # inherited method


# Example 2 – Child Adding Method
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Bike(Vehicle):
    def ride(self):
        print("Bike riding")

b = Bike()
b.start()
b.ride()


# Example 3 – Method Overriding
class Bird:
    def fly(self):
        print("Bird flying")

class Penguin(Bird):
    def fly(self):  # override parent method
        print("Penguin cannot fly")

p = Penguin()
p.fly()


# Example 4 – Multi-level Inheritance
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

c = C()
c.show()


# Example 5 – Inheriting Attributes
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    pass

t = Teacher("Ahmed")
print(t.name)


# ================================
# 3. COMPOSITION
# ================================

# Example 1
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has Engine

car = Car()
car.engine.start()


# Example 2
class CPU:
    pass

class Computer:
    def __init__(self):
        self.cpu = CPU()

pc = Computer()
print(pc.cpu)


# Example 3
class Address:
    def __init__(self, city):
        self.city = city

class Employee:
    def __init__(self, address):
        self.address = address

addr = Address("Lahore")
emp = Employee(addr)
print(emp.address.city)


# Example 4
class Battery:
    pass

class Phone:
    def __init__(self):
        self.battery = Battery()

ph = Phone()
print(ph.battery)


# Example 5
class Book:
    pass

class Library:
    def __init__(self):
        self.book = Book()

lib = Library()
print(lib.book)


# ================================
# 4. AGGREGATION
# ================================

# Example 1
class Student:
    pass

class School:
    def __init__(self, student):
        self.student = student

s = Student()
school = School(s)


# Example 2
class Author:
    pass

class Book:
    def __init__(self, author):
        self.author = author

a = Author()
b = Book(a)


# Example 3
class Player:
    pass

class Team:
    def __init__(self, player):
        self.player = player

p = Player()
team = Team(p)


# Example 4
class Teacher:
    pass

class Department:
    def __init__(self, teacher):
        self.teacher = teacher

t = Teacher()
dept = Department(t)


# Example 5
class Driver:
    pass

class Bus:
    def __init__(self, driver):
        self.driver = driver

d = Driver()
bus = Bus(d)


# ================================
# 5. METHODS
# ================================

# Example 1 – Instance Method
class Person:
    def greet(self):
        print("Hello")

p = Person()
p.greet()


# Example 2 – Method with Parameter
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))


# Example 3 – Method Using Attribute
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking")

d = Dog("Buddy")
d.bark()


# Example 4 – Class Method
class Company:
    name = "ABC"

    @classmethod
    def show_company(cls):
        print(cls.name)

Company.show_company()


# Example 5 – Static Method
class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

print(Math.multiply(4, 5))


# ================================
# 6. POLYMORPHISM
# ================================

# Example 1
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

# Example 2
for animal in [Dog(), Cat()]:
    animal.sound()


# Example 3
class Car:
    def move(self):
        print("Drive")

class Boat:
    def move(self):
        print("Sail")

for vehicle in [Car(), Boat()]:
    vehicle.move()


# Example 4
class Bird:
    def fly(self):
        print("Flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

for obj in [Bird(), Airplane()]:
    obj.fly()


# Example 5
class Shape:
    def area(self):
        pass


# ================================
# 7. SUPER()
# ================================

# Example 1
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

c = Child()
c.show()


# Example 2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ali", "A")
print(s.name, s.grade)


# Example 3
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()

b = B()
b.greet()


# Example 4
class Vehicle:
    def __init__(self):
        print("Vehicle created")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

car = Car()


# Example 5
class Shape:
    def area(self):
        print("Base area")

class Square(Shape):
    def area(self):
        super().area()

sq = Square()
sq.area()


# ================================
# 8. ABSTRACTION
# ================================

from abc import ABC, abstractmethod  # module for abstract classes

# Example 1
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


# Example 2
class Dog(Animal):
    def sound(self):
        print("Bark")


# Example 3
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Example 4
class Circle(Shape):
    def area(self):
        print("Area of circle")


# Example 5
class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")


# testing abstraction classes
d = Dog()
d.sound()

c = Circle()
c.area()

r = Rectangle()
r.area()