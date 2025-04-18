class Car:
    color = "red"  # class variable
    wheels = 4  # class variable
    model = "Toyota"  # class variable
    make = "Corolla"  # class variable
#Methods/behavior of the class
    def drive(self):
        print("The car is driving")
my_car = Car()  # creating an object of the class
my_car.drive()  # calling the method of the class
print(my_car.wheels)  # accessing class variable using object


class Person:
    def __init__(self, name, age, height):
        self.name = name    # Instance variable
        self.age = age # Instance variable
        self.height = height

persondetails = Person("John", 30, 160)  # creating an object of the class
print(persondetails.height)  # accessing instance variable using object
