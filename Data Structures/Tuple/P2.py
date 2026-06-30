# Write a program to check whether an element exists in a tuple or not.
Tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tuple:", Tuple)
element = int(input("Enter an element to check: "))
if element in Tuple:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")