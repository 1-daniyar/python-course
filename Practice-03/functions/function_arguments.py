# function_arguments.py
# Positional and default arguments

# Positional arguments: order matters
def full_name(first, last):
    """Combines first and last name."""
    return f"{first} {last}"

print(full_name("John", "Doe"))


# Default arguments: used when no value is passed
def power(base, exponent=2):
    """Raises base to exponent. Defaults to squaring."""
    return base ** exponent

print(power(4))      # uses default exponent 2 -> 16
print(power(2, 5))   # 2^5 -> 32


# Keyword arguments: pass by name, order doesn't matter
def order_food(dish, drink):
    """Prints a food order."""
    print(f"You ordered {dish} with {drink}")

order_food(drink="cola", dish="pizza")


# Passing a list as an argument
def total_price(prices):
    """Returns the sum of a list of prices."""
    return sum(prices)

print("Total:", total_price([100, 250, 75]))
