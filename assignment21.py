"""Q1 . Ask the user for a string and check whether it is a palindrome or not.
(A palindrome is a string which is same when we read it forward & backward. Eg - “madam”, “racecar” etc.)
"""
def is_palindrome(s):
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False
s = input("Enter the string:").upper()
print(is_palindrome(s))