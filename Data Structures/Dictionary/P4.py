# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
dict = {0:10, 1:20, 2:30, 3:40, 4:50}

print("Keys are:")
for i in dict:
    print(i)

print("Values are:")
for i in dict:
    print(dict[i])

print("Keys and Values are:")
for i in dict:
    print(i, ":", dict[i])