# generators.py
# Iterators and Generators

# ---------- ITERATORS ----------

# An iterator lets you go through items one at a time using next()
my_list = [10, 20, 30]
my_iter = iter(my_list)        # get an iterator from a list

print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# next(my_iter) here would raise StopIteration


# Looping through an iterator (a for loop does iter()/next() for you)
for item in iter(["a", "b", "c"]):
    print(item)


# Creating your OWN iterator with __iter__ and __next__
class Countdown:
    """Counts down from a starting number to 1."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # the object is its own iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration   # signals the loop to stop
        value = self.current
        self.current -= 1
        return value

print("Countdown:")
for number in Countdown(5):
    print(number)


# ---------- GENERATORS ----------

# A generator function uses 'yield' instead of 'return'.
# It produces values lazily, one at a time.
def count_up_to(limit):
    """Yields numbers from 1 up to limit."""
    n = 1
    while n <= limit:
        yield n      # pauses here and returns n, resumes on next call
        n += 1

print("Generator function:")
for num in count_up_to(5):
    print(num)


# Generator that produces an infinite-ish sequence (Fibonacci)
def fibonacci(count):
    """Yields the first 'count' Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

print("Fibonacci:", list(fibonacci(8)))


# ---------- GENERATOR EXPRESSIONS ----------

# Like a list comprehension but with () — saves memory
squares_gen = (x * x for x in range(1, 6))
print("Squares from generator expression:", list(squares_gen))

# Useful directly inside functions like sum()
total = sum(x for x in range(1, 101))
print("Sum 1..100:", total)
