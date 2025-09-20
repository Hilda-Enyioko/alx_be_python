# Objective:  Utilize while loops and nested for loops to draw a simple text-based pattern.

pattern_size = int(input("Enter the size of the pattern: "))

row = 0
while (row < pattern_size):
    for i in range(0, pattern_size):
        print("*", end="")
    print()
    row += 1