"""Design a program to continuously input a number 'n'
from user & print if it is positive or negative until the user enters “Quit”."""
while True:
    user_input = input("Enter number: ")

    if user_input == "Quit":
        print("Exiting the program.")
        break

    n = int(user_input)

    if n < 0:
        print("Negative")
    elif n > 0:
        print("Positive")
    else:
        print("Zero")
