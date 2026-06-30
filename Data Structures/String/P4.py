# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
String = (str(input("Enter the string: ")))
if String[0] == 'x' and String[-1] == 'x':
    String = String[1:-1]
    print(String)
else:
    print(String)       