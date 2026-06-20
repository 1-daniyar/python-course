# lambda_with_filter.py
# Using lambda with filter() to select items

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)


# Keep numbers greater than 5
big = list(filter(lambda x: x > 5, numbers))
print("Greater than 5:", big)


# Filter out empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda w: w != "", words))
print("Non-empty:", non_empty)


# Filter names that start with 'A'
names = ["Aisha", "Bob", "Anna", "Charlie", "Alex"]
a_names = list(filter(lambda n: n.startswith("A"), names))
print("Names with A:", a_names)
