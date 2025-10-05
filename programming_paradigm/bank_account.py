# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.
# Check ./main-0.py for usage
class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = float(account_balance)
        self.initial_balance = float(initial_balance)
        
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        
        else:
            self.account_balance -= amount
            return True
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
