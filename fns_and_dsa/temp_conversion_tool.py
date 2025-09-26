# Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
result_temp = 0

def  convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    result_temp = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return result_temp

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    result_temp = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return result_temp

def main():
    temperature = int(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if unit == "C":
        convert_to_celsius()
    elif unit == "F":
        convert_to_fahrenheit()