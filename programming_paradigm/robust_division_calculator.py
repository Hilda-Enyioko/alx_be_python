# Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
# Check ./main-1.py for usage

def safe_divide(numerator, denominator):
    try:
        dividend = float(numerator)
        divisor = float(denominator)
        quotient = dividend / divisor
        return(f"The result of the division is {quotient}")

    except ValueError:
        return("Error: Please enter numeric values only.")
    
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")