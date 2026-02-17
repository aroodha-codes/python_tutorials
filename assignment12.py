"""Q2 Write a function that takes two integers a and b
and prints all even numbers between them (inclusive).
"""
def even_no(a,b):
    for i in range(a,b):
        if (i%2==0):
            print(i)
even_no(1,10)