# multiple_inheritance.py
# A class inheriting from more than one parent

class Engine:
    """Provides engine behavior."""
    def start_engine(self):
        print("Engine started.")

class Radio:
    """Provides radio behavior."""
    def play_music(self):
        print("Playing music.")

# Car inherits from BOTH Engine and Radio
class Car(Engine, Radio):
    """A car that combines Engine and Radio features."""
    def drive(self):
        print("Driving the car.")

my_car = Car()
my_car.start_engine()  # from Engine
my_car.play_music()    # from Radio
my_car.drive()         # from Car itself
