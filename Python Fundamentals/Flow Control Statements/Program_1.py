# Write a program to check if a given number is Positive, Negative, or Zero.
def check_number(number):
    if number > 0:
      print(f"The number ({number}) is positive.")
    elif number < 0:
      print(f"The number ({number}) is negative.")
    else:
      print(f"The number ({number}) is zero.")

if __name__ == "__main__":
    number = [1, -5, 0, 10, -3]
    for n in number:
        check_number(n)    