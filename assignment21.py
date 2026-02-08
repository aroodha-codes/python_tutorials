"""Q1 . Ask the user for a string and check whether it is a palindrome or not.
(A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.)
"""
s = input("Enter the word:")
rev = s[::-1]
if s == rev:
    print("Plaindrome")
else:
    print("Non-Palindrome")