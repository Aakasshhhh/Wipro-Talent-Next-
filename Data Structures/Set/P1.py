# Write a program to remove a given item from the set.
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s = 5
if s in set:
    set.remove(s)
print(set)