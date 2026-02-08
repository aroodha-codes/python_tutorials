# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute 
# simple interest:SI = (P ∗ R ∗ T )/100
P = float(input("Enter the principle Amount:"))
R = float(input("Enter the rate:"))
T = float(input("Enter the time in years:"))
SI = (P*R*T)/100
print("The simple interest is:",SI)
print("Total Amount is : ",P+SI)
