# Write a program to reverse the order of the items in the list.
list = [4, 3, 7, 4, 7, 3, 9]
reversed_list = []
for i in range(len(list)-1, -1, -1):
    reversed_list.append(list[i])

print("Original List:", list)
print("Reversed List:", reversed_list)