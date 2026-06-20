# inheritance_basics.py
# Parent and child class relationships

# Parent (base) class
class Animal:
    """A generic animal."""
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child (derived) class inherits from Animal
class Cat(Animal):
    """A cat that inherits from Animal."""
    def meow(self):
        print(f"{self.name} says Meow!")

# The child has access to both its own and the parent's methods
my_cat = Cat("Whiskers")
my_cat.eat()    # inherited from Animal
my_cat.meow()   # defined in Cat
