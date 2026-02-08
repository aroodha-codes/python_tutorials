"""
Q10. Ask the user for a string and print:
•All unique characters
•The count of unique characters
"""
string = input("Enter the string:")
unique = set()
for s in  string:
    if (s not in unique):
        unique.add(s)
print(f"Unique elements are:{unique} and count is :{len(unique)}")
