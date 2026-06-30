# Write a program to convert a list into a tuple.
List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tuple = ()
for i in List:
    tuple += (i,)
print("List:", List)
print("Tuple:", tuple)