import sys
if len(sys.argv) > 1:
    # Input from command-line arguments
    input_marks = sys.argv[1:]
    marks = list(map(int, input_marks))
else:
    marks = [50, 60, 70, 80, 90]
print("You entered the marks:", marks)
total = sum(marks)
average = total / len(marks)
maximum = max(marks)
minimum = min(marks)
print("Total =", total)
print("Average =", average)
print("Maximum value =", maximum)
print("Minimum value =", minimum)
print("Maximum – Minimum =", maximum - minimum)
