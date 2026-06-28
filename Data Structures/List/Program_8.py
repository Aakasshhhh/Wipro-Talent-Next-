# Write a program to remove the first occurrence of a specified element from a list.


list = [1, 2, 3, 1, 2, 3, 4, 5, 4, 3, 4, 5, 6, 8, 7, 9, 0, 4, 1, 3, 2, 3, 4, 5, 6, 7, 9, 0]
element = (4)
index = list.index(element)
print("Index which removed:", index)
    
if element in list:
    list.remove(element)
    print(f"First occurrence of element {element} removed.")