""" Let's create a "Number Guessing Game" Given a secret number (already 
decided by you), write a program that asks the user to guess it and prints:
"Too high" if the guess is above the number
"Too low" if the guess is below
"Correct!" if the guess matches """
secret_number = 9
guess = int(input("Enter the Guess Number:"))
if (secret_number == guess):
    print("Correct!")
elif (secret_number < guess):
    print("Too high")
elif (secret_number > guess):
    print("Too low")
