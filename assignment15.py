"""Q5.Write a function to return the sum of digits of a number,n."""
def calc_sum(n):
    sum = 0
    while(n > 0):
        p = n%10
        sum += p
        n = n//10
    print(sum)
n = int(input("Enter n:"))
calc_sum(n)