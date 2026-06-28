# Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
list = [10, 20, 30, 40, 50]
print("List contents:")
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")