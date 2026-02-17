"""Ask the user for a temperature in Celsius (string input). Convert it to 
float, then calculate and print temperature in Fahrenheit
Conversion formula:
 Fahrenheit Temp = (Celsius Temp * (9/5)) + 32"""
Celsius = int(input("Enter the Temperature in celsius:"))
Celsius=float(Celsius)
Fahrenheit = (Celsius * (9/5)) + 32
print("The Temperature in Fahrenheit is:",Fahrenheit)