# Write a program to count the number of upper and lower case letters in a String.
String =  (str(input("Enter the string: ")))
upper_count = 0
lower_count = 0

for char in String:
    if char >= 'a' and char <= 'z':
        lower_count += 1
    elif char >= 'A' and char <= 'Z':
        upper_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)