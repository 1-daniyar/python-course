# args_kwargs.py
# *args and **kwargs for flexible arguments

# *args collects extra positional arguments into a tuple
def add_all(*numbers):
    """Adds any number of arguments together."""
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))


# **kwargs collects extra keyword arguments into a dictionary
def print_info(**details):
    """Prints all key-value pairs passed in."""
    for key, value in details.items():
        print(f"{key}: {value}")

print_info(name="Aisha", age=21, city="Taraz")


# Combining normal args, *args, and **kwargs
def make_profile(username, *hobbies, **info):
    """Builds a profile from mixed argument types."""
    print("User:", username)
    print("Hobbies:", hobbies)
    print("Info:", info)

make_profile("dt_qotir", "coding", "reading", country="KZ", level="student")
