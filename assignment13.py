"""Write a function that prints the digits of a number,n.
For eg: n = 312, there are 3 digits in it 3, 1 and 2 & we need to print them."""

def print_digits(n):
    while(n > 0):
        p=n%10
        print(p)
        n=n//10
n = int(input("Enter n:"))
print_digits(n)
