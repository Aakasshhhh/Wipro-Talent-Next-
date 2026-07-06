#Write a function to return the reverse of a string.  
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_string(s):
   rev = ""
   for i in s:
       rev = i + rev
   return rev

# Test the function


sample_string = "1234abcd"
print(reverse_string(sample_string))  