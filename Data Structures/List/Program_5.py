# Write a program to append the items of list1 to list2 in the front.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = []

for i in list1:
    new_list = new_list + [i]
for j in list2:
    new_list = new_list + [j]

print("new_list:", new_list)