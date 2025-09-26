# Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %M:%H:%S")
    print(f"Current date: {current_date}")

def calculate_future_date():
    start_date = datetime.now()
    added_days = int(input("Enter the number of days to add to the current date: "))
    future_date =  (start_date + timedelta(days=added_days)).strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()