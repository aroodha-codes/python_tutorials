#Write a program to swap values of two numbers entered by the user.
a = int(input("Enter A:"))
b = int(input("Enter B:"))
print(a)
print(b)
temp = a
a = b
b = temp
print("Values after swapping:")
print(a)
print(b)