# Write a program to print prime numbers between 10 and 99.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Prime numbers between 10 and 99:")
    for n in range(10, 100):
        if is_prime(n):
            print(n)