# Write a program to append a new item to the end of the list.
list = [10, 20, 30, 40, 50]
print("List contents:")
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")
new_item = 60
list.append(new_item)
print("Updated List contents:") 
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")   

more_items = int(input("Enter the new number: "))
list.append(more_items)
print("Updated List contents:")
for i in range(len(list)):
    print(f"Element at index {i}: {list[i]}")   
    