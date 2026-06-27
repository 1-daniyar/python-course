"""
Practice 6 - Built-in Functions
builtin_functions/enumerate_zip_examples.py

Demonstrates paired / indexed iteration:
  - enumerate()  index + value while looping
  - zip()        iterate several sequences in parallel
  - zip(*...)    "unzip" back into separate sequences
  - dict(zip(...)) build a dictionary from two lists

Run:
    python enumerate_zip_examples.py
"""

fruits = ["apple", "banana", "cherry"]
prices = [120, 80, 200]
stock = [50, 30, 15]


def use_enumerate():
    print("--- enumerate(): index + value ---")
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")

    print("\n--- enumerate() with custom start ---")
    for rank, fruit in enumerate(fruits, start=1):
        print(f"  #{rank} {fruit}")


def use_zip():
    print("\n--- zip(): iterate two lists together ---")
    for fruit, price in zip(fruits, prices):
        print(f"  {fruit}: {price} KZT")

    print("\n--- zip(): three lists together ---")
    for fruit, price, qty in zip(fruits, prices, stock):
        print(f"  {fruit:8} price={price:4}  stock={qty}")


def combine_enumerate_zip():
    print("\n--- enumerate() + zip() together ---")
    for i, (fruit, price) in enumerate(zip(fruits, prices), start=1):
        print(f"  {i}. {fruit} costs {price} KZT")


def unzip():
    print("\n--- Unzip with zip(*...) ---")
    pairs = list(zip(fruits, prices))
    print("pairs:", pairs)
    names, costs = zip(*pairs)
    print("names:", names)
    print("costs:", costs)


def build_dict():
    print("\n--- dict(zip(...)): make a dictionary ---")
    catalog = dict(zip(fruits, prices))
    print("catalog:", catalog)

    # total inventory value using zip + sum
    total_value = sum(price * qty for price, qty in zip(prices, stock))
    print("total inventory value:", total_value, "KZT")


def main():
    use_enumerate()
    use_zip()
    combine_enumerate_zip()
    unzip()
    build_dict()


if __name__ == "__main__":
    main()
