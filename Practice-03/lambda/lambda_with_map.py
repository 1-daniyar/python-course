# lambda_with_map.py
# Using lambda with map() to transform every item

numbers = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print("Fahrenheit:", fahrenheit)


# Uppercase a list of words
words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda w: w.upper(), words))
print("Uppercase:", upper_words)


# map() with two lists at once
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print("Pairwise sums:", sums)
