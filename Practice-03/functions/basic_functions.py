# basic_functions.py
# Defining and calling functions

# A simple function with no arguments
def greet():
    """Prints a greeting message."""
    print("Hello, world!")

greet()  # calling the function


# A function with one argument
def greet_person(name):
    """Greets a specific person by name."""
    print(f"Hello, {name}!")

greet_person("Aisha")


# A function that uses a return value
def square(number):
    """Returns the square of a number."""
    return number * number

result = square(5)
print("Square of 5 is:", result)


# A function calling another function
def describe_square(number):
    """Describes the square of a number using square()."""
    print(f"The square of {number} is {square(number)}")

describe_square(7)
