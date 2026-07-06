# Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print("Factorial of 5:", factorial(5))
print("Factorial of -4:", factorial(-4))