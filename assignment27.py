"""Q7 . Write a program that takes a string from the user 
and prints the number of spaces in the string.
"""
string = input("Enter the string:")
count = 0
for s in string:
    if (s == " "):
        count += 1
print(count)
