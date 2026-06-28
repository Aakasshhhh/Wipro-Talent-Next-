# Write a program to reverse a given number and print.
# Example:1
# I/P: 1234
# O/P:4321

# Example:2
# I/P:1004
# O/P:4001

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

if __name__ == "__main__":
    numbers = (1526, 83, 9383, 0000, 2348, 8363)
    for n in numbers:
        print(f"Reversed number of {n}: {reverse_number(n)}")   