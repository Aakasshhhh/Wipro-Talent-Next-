# Write a program that will check whether a given String is Palindrome or not.
String = ("abcdcba", 'jalaj', "manas")
for s in String:
    rev = ""
    for i in s:
        rev = i + rev
    if s == rev:
        print(s, "is a Palindrome")
    else:
        print(s, "is not a Palindrome")