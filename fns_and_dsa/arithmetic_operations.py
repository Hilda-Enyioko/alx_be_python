# Objective: A python script to define a function that performs basic arithmetic operations. 

def perform_operation(num1, num2, operation):
    result = 0
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num2 == 0:
                return "Any number divided by 0 gives infinity"
            else:
                result = num1 / num2
        case _:
            return "Enter a valid operation (add, subtract, multiply, divide)"
    
    return result