""" 
Q1 Write a program that takes salary as input. Using conditional statements, calculate the
final tax rate based on these rules:
•If salary < 30,000 → 5%
•If salary is 30,000-70,000 →15%
•If salary > 70,000 →25% 
"""
salary = int(input("Enter the Salary of person:"))
if (salary < 30000):
    tax_rate = salary*0.05
    print("The tax rate is:",tax_rate)
elif (salary >= 30000 and salary<=70000):
    tax_rate = salary*0.15
    print("The tax rate is:",tax_rate)
else:
    tax_rate = salary*0.25
    print("The tax rate is:",tax_rate)
"""
salary = int(input("Enter the Salary of person: "))

if salary < 30000:
    rate = 0.05
elif salary <= 70000:
    rate = 0.15
else:
    rate = 0.25

tax = salary * rate
print("The tax rate is:", tax)"""
