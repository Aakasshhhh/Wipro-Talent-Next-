#Write a function to return the sum of all numbers in a list.  
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total        

# Test the function
sample_list = (8, 2, 3, 0, 7)
print(sum_of_list(sample_list))  # Expected Output: 20