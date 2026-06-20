# class_methods.py
# Instance methods and modifying/deleting properties

class BankAccount:
    """A simple bank account."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        """Removes money if there are enough funds."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")

account = BankAccount("Aisha", 1000)
account.deposit(500)
account.withdraw(300)

# Modifying a property directly
account.owner = "Aisha K."
print("Owner updated to:", account.owner)

# Deleting a property
del account.owner
# print(account.owner)  # would now raise an AttributeError
print("Owner attribute deleted.")
