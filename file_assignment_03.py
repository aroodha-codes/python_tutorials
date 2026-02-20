"""
Q3. Create a program that:
Has a list of numbers: [5, 10, 15, 20, 25]
Uses a list comprehension to create a new list with only numbers greater than 15
Prints the new list
"""
numbers = [5,10,15,20,25]
new_list = [n for n in numbers if n > 15]
print(new_list)