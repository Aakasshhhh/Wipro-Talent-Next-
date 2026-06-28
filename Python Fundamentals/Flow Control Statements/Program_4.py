# Write a program to print numbers from 1 to 10 in a single row with one tab space.
def print_numbers():
    for i in range(1, 11):
        print(i, end="\t")

if __name__ == "__main__":
    print("Numbers from 1 to 10:")
    print_numbers()