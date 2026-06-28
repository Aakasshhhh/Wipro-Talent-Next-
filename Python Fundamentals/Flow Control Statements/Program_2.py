# Write a program to check if a given number is odd or even.
def check_odd_even(number):
    if number % 2 == 0:
        print(f"The number ({number}) is even.")
    else:
        print(f"The number ({number}) is odd.")

if __name__ == "__main__":
    number = [8, 21, 0, 55, 100, -2, -91]
    for n in number:
        check_odd_even(n)