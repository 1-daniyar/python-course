# class_definition.py
# Defining a class and creating objects

# Define a simple class
class Dog:
    """Represents a dog."""
    def bark(self):
        print("Woof!")

# Create objects (instances) of the class
dog1 = Dog()
dog2 = Dog()

dog1.bark()
dog2.bark()


# A class with an attribute set after creation
class Car:
    """Represents a car."""
    pass

my_car = Car()
my_car.brand = "Toyota"   # adding an attribute to the object
my_car.color = "red"
print(f"My car is a {my_car.color} {my_car.brand}")
