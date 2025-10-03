# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

class BankAccount:
    def __init__(self, account_balance, initial_balance = 0):
        self.account_balance = account_balance,
        self.initial_balance = initial_balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            print ("Insufficient funds")
            return False
        
        else:
            self.account_balance -= amount
            print (self.account_balance)
            return True
    
    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"
