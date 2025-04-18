# Week 5 Assignment: Object-Oriented Programming (OOP) in Python
# 1.Assignment 1: Design Your Own Class! 🏗️
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old and {self.height}cm tall."

# Subclass
class Superhero(Person):
    def __init__(self, name, age, height, superpower):
        super().__init__(name, age, height)
        self.superpower = superpower

    def introduce(self):
        return f"I am {self.name}, a superhero with the power of {self.superpower}!"

    
    def use_power(self):
        return f"{self.name} uses {self.superpower}!"

# Creating objects
person1 = Person("Kaiser", 30, 170)
hero1 = Superhero("Nova", 28, 180, "Invisibility")


print(person1.introduce())     
print(hero1.introduce())       
print(hero1.use_power())       


#Activity 2: Polymorphism Challenge!
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in action
for animal in [Dog(), Cat()]:
    print(animal.speak())