import sys

# Check if command-line arguments are passed
if len(sys.argv) > 1:
    # Input from command-line arguments
    input_marks = sys.argv[1:]
    marks = list(map(int, input_marks))
else:
    # Input from user
    marks = [50, 60, 70, 80, 90]

print("You entered the marks:", marks)

# Sum of marks
total = sum(marks)

# Average
average = total / len(marks)

# Maximum and Minimum
maximum = max(marks)
minimum = min(marks)

print("Total =", total)
print("Average =", average)
print("Maximum value =", maximum)
print("Minimum value =", minimum)
print("Maximum – Minimum =", maximum - minimum)
