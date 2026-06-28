# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def last_digit(num1, num2):
    if num1 % 10 == num2 % 10:
        print(f"The numbers ({num1}) and ({num2}) have the same last digit.")
    else:
        print(f"The numbers ({num1}) and ({num2}) do not have the same last digit.")

if __name__ == "__main__":
    numbers = [(27, 57), (6, 17), (3, 113), (10, 20), (45, 55)]
    for num1, num2 in numbers:
        last_digit(num1, num2)  