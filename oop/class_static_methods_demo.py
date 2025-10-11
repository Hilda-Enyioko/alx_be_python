# Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.
# See main-3.py for usage example.

class Calculator:
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print (f"Calculation Type: {cls.calculation_type}")
        return a * b