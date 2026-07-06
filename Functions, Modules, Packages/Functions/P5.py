# Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]      
def print_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print_even_numbers(list))  