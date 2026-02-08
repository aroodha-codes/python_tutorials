"""Take a decimal number as input (like 45.78) and output its:
•integer part -45
• fractional part -.78"""
num =  float(input("Enter the number:"))
int_part = int(num)
float_part = num - int_part
print("Integer part:",int_part)
print("Float part:%.2f" %float_part)
