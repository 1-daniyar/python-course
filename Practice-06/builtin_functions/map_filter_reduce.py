"""
Practice 6 - Built-in Functions
builtin_functions/map_filter_reduce.py

Demonstrates data-processing built-ins:
  - map()     apply a function to every item
  - filter()  keep items that pass a test
  - reduce()  aggregate a sequence to one value (from functools)
  - len(), sum(), min(), max(), sorted()
  - type conversion: int(), float(), str(), list(), tuple(), set(), bool()

Run:
    python map_filter_reduce.py
"""

from functools import reduce

numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]


def aggregation():
    print("--- Aggregation built-ins ---")
    print("numbers :", numbers)
    print("len()   :", len(numbers))
    print("sum()   :", sum(numbers))
    print("min()   :", min(numbers))
    print("max()   :", max(numbers))
    print("sorted():", sorted(numbers))
    print("sorted desc:", sorted(numbers, reverse=True))


def use_map():
    print("\n--- map(): apply a function to each item ---")
    squares = list(map(lambda x: x ** 2, numbers))
    print("squares     :", squares)

    words = ["apple", "banana", "cherry"]
    lengths = list(map(len, words))
    print("word lengths:", lengths)

    # map over two lists in parallel
    a, b = [1, 2, 3], [10, 20, 30]
    sums = list(map(lambda x, y: x + y, a, b))
    print("pairwise sum:", sums)


def use_filter():
    print("\n--- filter(): keep items passing a test ---")
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("even numbers:", evens)

    words = ["hi", "hello", "hey", "greetings"]
    long_words = list(filter(lambda w: len(w) > 3, words))
    print("words > 3 chars:", long_words)


def use_reduce():
    print("\n--- reduce(): fold a sequence into one value ---")
    product = reduce(lambda acc, x: acc * x, numbers, 1)
    print("product of all:", product)

    total = reduce(lambda acc, x: acc + x, numbers, 0)
    print("sum via reduce:", total)

    biggest = reduce(lambda acc, x: x if x > acc else acc, numbers)
    print("max via reduce:", biggest)


def type_conversions():
    print("\n--- Type conversions ---")
    print('int("42")     =', int("42"))
    print('float("3.14") =', float("3.14"))
    print("str(99)       =", str(99))
    print('list("abc")   =', list("abc"))
    print("tuple([1,2])  =", tuple([1, 2]))
    print("set([1,1,2])  =", set([1, 1, 2]))
    print("bool(0)       =", bool(0), "| bool(5) =", bool(5))

    print("\n--- Type checking ---")
    samples = [42, 3.14, "text", [1, 2], {"k": 1}]
    for s in samples:
        print(f"  {str(s):10} -> type {type(s).__name__:5} | isinstance int? {isinstance(s, int)}")


def main():
    aggregation()
    use_map()
    use_filter()
    use_reduce()
    type_conversions()


if __name__ == "__main__":
    main()
