# Write a function that takes a number as a parameter and checks whether the number is prime or not.
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it is prime: "))
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")