"""The user enters a string containing a number (e.g."45",). Convert it to:
•an integer
•a float
•a string again
Print all three values with their types."""
A = input("Enter a string containing number:")
B = int(A)
C = float(A)
D = str(A)
print(B,type(B))
print(C,type(C))
print(D,type(D))