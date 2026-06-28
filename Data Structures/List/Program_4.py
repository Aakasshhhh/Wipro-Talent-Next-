# Write a program to print the number of occurrences of a specified element in a list.
list = [1, 2, 3, 4, 5, 2, 3, 2, 6, 7, 2, 8, 9, 2, 10, 2, 11, 2, 12, 2, 13, 2, 14, 2, 15, 2, 16, 2, 17, 2, 18, 2, 19, 2, 20]
element = int(input("Enter the element to count occurrences: "))
count = 0
for i in list:
    if i == element:
        count += 1
print(f"The element {element} occurs {count} times in the list.")