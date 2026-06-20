# init_method.py
# The __init__() constructor and the self parameter

class Person:
    """Represents a person with a name and age."""
    def __init__(self, name, age):
        # self refers to the specific object being created
        self.name = name
        self.age = age

    def introduce(self):
        """Prints an introduction."""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# __init__ runs automatically when the object is created
p1 = Person("Aisha", 21)
p2 = Person("Bob", 19)

p1.introduce()
p2.introduce()

# Accessing attributes directly
print(p1.name, "is", p1.age)
