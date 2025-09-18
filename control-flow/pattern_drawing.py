# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to go through rows
while row < size:
    # Use for loop to print stars in each row
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to next line after finishing a row
    row += 1