# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it. 
def count_case(s):
    upper_case_count = 0
    lower_case_count = 0
    
    for char in s:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
            
    print("Number of Upper case letters:", upper_case_count)
    print("Number of Lower case letters:", lower_case_count)

    return upper_case_count, lower_case_count

count_case("Data Science with Python")