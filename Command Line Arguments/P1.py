# Write a program to accept two numbers as command line arguments and display their sum.
import sys
if len(sys.argv) != 3:
    print("Please provide exactly two numbers as command line arguments.")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
sum = num1 + num2
print("Sum =", sum)