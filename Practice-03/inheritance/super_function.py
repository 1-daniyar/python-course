# super_function.py
# Using super() to call the parent class methods

class Vehicle:
    """A generic vehicle."""
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle created: {self.brand}")

class Car(Vehicle):
    """A car that extends Vehicle."""
    def __init__(self, brand, model):
        # Call the parent's __init__ to reuse its setup
        super().__init__(brand)
        self.model = model
        print(f"Car details: {self.brand} {self.model}")

my_car = Car("Toyota", "Corolla")
print(f"Final: {my_car.brand} {my_car.model}")
