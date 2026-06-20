# return_values.py
# Return statements and return values

# Returning a single value
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add(3, 4))


# Returning multiple values (as a tuple)
def min_max(numbers):
    """Returns both the minimum and maximum of a list."""
    return min(numbers), max(numbers)

low, high = min_max([5, 1, 9, 3])
print("Min:", low, "Max:", high)


# A function with no return returns None
def say_hi():
    """Prints but returns nothing."""
    print("Hi")

value = say_hi()
print("Returned value:", value)  # None


# Using return to exit early
def check_age(age):
    """Returns a label based on age, exiting early if underage."""
    if age < 18:
        return "Minor"
    return "Adult"

print(check_age(15))
print(check_age(30))
