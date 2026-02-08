"""Let's create a Simple Calculator that performs arithmetic operations.
Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division based on the
operation parameter.
operation parameter can have values '+', '-','*' ,'/'"""

def calci(a,b,operation):
    if (operation == '+'):
        ans = a + b
    elif (operation == '-'):
        ans = a - b
    elif (operation == '*'):
        if(a and b != 0):
            ans = a * b
        else:
            print("Error")
    elif (operation == '/'):
        if(b != 0):
            ans = a / b
        else:
            print("Error")
    else:
        print("Exiting...")        
    return ans
print(calci(5,5,'+'))
print(calci(8,2,'-'))
print(calci(3,4,'*'))
print(calci(3,4,'/'))