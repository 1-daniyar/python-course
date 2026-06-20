# class_variables.py
# Class variables vs instance variables

class Student:
    """Demonstrates the difference between class and instance variables."""

    # Class variable: shared by ALL instances
    school = "Tech University"

    def __init__(self, name):
        # Instance variable: unique to EACH object
        self.name = name

s1 = Student("Aisha")
s2 = Student("Bob")

# Instance variables differ per object
print(s1.name, "-", s1.school)
print(s2.name, "-", s2.school)

# Changing the class variable affects all instances
Student.school = "New Tech University"
print(s1.name, "-", s1.school)
print(s2.name, "-", s2.school)

# But overriding it on one instance only affects that instance
s1.school = "Private Academy"
print(s1.name, "-", s1.school)  # changed
print(s2.name, "-", s2.school)  # unchanged
