# method_overriding.py
# Overriding a parent method in the child class

class Shape:
    """A generic shape."""
    def area(self):
        """Default area, meant to be overridden."""
        return 0

    def describe(self):
        print(f"This shape has an area of {self.area()}")

class Rectangle(Shape):
    """A rectangle that overrides area()."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # overrides Shape.area()
        return self.width * self.height

class Circle(Shape):
    """A circle that overrides area()."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # overrides Shape.area()
        return 3.14159 * self.radius ** 2

rect = Rectangle(4, 5)
circle = Circle(3)

rect.describe()
circle.describe()
