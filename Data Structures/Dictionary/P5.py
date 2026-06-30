# Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
dict = {}
i=1
while i<=15:
    dict[i] = i*i
    i = i+1
print(dict)