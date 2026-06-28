# Write a program to find if the given number is palindrome or not
# Example:1
# I/P:110011
# O/P: 110011 is a palindrome.

# Example:2
# I/P:1234
# O/P: 1234 is not a palindrome.

def is_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + (n % 10)
        n //= 10
    return original == reversed_num

if __name__ == "__main__":
    numbers = (110011, 1234, 98789, 45654, 12321, 1001)
    index = 0
    while index < len(numbers):
        n = numbers[index]
        if is_palindrome(n):
            print(f"{n} is a palindrome.")
        else:
            print(f"{n} is not a palindrome.")
        index += 1  