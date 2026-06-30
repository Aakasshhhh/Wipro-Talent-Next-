# Write a program to check if a given key already exists in a dictionary.

dict1 = {0:10, 1:20, 2:30, 3:40, 4:50, 5:60, 6:70, 7:80, 8:90, 9:100}
key_to_check = int(input("Enter the key to check: "))

if key_to_check in dict1:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")