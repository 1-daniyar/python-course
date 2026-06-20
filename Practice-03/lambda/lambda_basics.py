# lambda_basics.py
# Lambda (anonymous) function basics

# Syntax: lambda arguments: expression

# A lambda that squares a number
square = lambda x: x * x
print(square(6))


# A lambda with two arguments
add = lambda a, b: a + b
print(add(3, 7))


# A lambda with a default argument
greet = lambda name="friend": f"Hello, {name}!"
print(greet())
print(greet("Aisha"))


# Lambda used immediately (inline)
print((lambda x: x + 100)(5))


# Regular function vs lambda — same result
def double_func(x):
    return x * 2

double_lambda = lambda x: x * 2

print(double_func(4), double_lambda(4))
