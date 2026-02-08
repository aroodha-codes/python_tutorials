"""Write a function to return the count the number of digits in a number, n."""

def count_no(n):
    count=0
    while(n > 0):
        count += 1
        n=n//10
    print(count)
n = int(input("Enter n:"))
count_no(n)
