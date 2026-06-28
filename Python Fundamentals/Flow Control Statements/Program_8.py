# Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == "__main__":
    number = (1234, 5678, 9876, 4321, 1111)
    for n in number:
        print(f"Sum of digits in {n}: {sum_of_digits(n)}")