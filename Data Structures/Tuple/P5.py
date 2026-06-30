# Write a program to replace last value of tuples in a list to 100.  
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
List = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]       
new_list = []
for i in List:
    t = (i[0], i[1], 100)
    new_list += [t]
print("Original List:", List)
print("Modified List:", new_list)