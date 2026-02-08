def calc_avg(a,b,c):
    average = (a+b+c)/3
    return average
A = int(input("Enter A:"))
B = int(input("Enter B:"))
C = int(input("Enter C:"))
print("The average of these numbers is:",calc_avg(A,B,C))