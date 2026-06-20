# lambda_with_sorted.py
# Using lambda with sorted() for custom sorting

# Sort numbers normally
numbers = [5, 2, 9, 1, 7]
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))


# Sort words by length
words = ["banana", "kiwi", "apple", "fig"]
print("By length:", sorted(words, key=lambda w: len(w)))


# Sort a list of tuples by the second element
scores = [("Aisha", 85), ("Bob", 72), ("Anna", 95)]
print("By score:", sorted(scores, key=lambda item: item[1]))


# Sort a list of dictionaries by a key
people = [
    {"name": "Aisha", "age": 21},
    {"name": "Bob", "age": 19},
    {"name": "Anna", "age": 25},
]
print("By age:", sorted(people, key=lambda p: p["age"]))
