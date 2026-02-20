# try exception else handling.
try:
    x= int(input("Enter the number:"))
    ans= 10/x
except ZeroDivisionError:
    print("Divide by Zero is not allowed.")
except ValueError:
    print("Enter the valid number.")
else:
    print(f"Answer is : {ans}")
finally:
    print("The program ended.")