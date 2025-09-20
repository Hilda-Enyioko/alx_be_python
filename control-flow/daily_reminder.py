# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

task = input("Describe your most important task for today: ")
priority = input("What is the priority level of this task (high, medium, low)? ").lower()
time_bound = input("Is this task time-bound (yes/no)? ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Note: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a high priority task. Make sure to complete it on time.")
    case "medium":
        if time_bound == "yes":
            print(f"Note: {task} is a medium priority task that should be completed soon.")
        else:
            print(f"Note: {task} is a medium priority task. Don't forget to finish it.")
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task, but it still needs to be done.")
        else:
            print(f"Note: {task} is a low priority task. You can take your time with it.")