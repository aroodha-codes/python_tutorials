# Polymorphism 
# Example - Operator Overloading
print(1 + 2)    # adds 2 numbers
print("1" + "2") # concatenates 2 strings
# 1. function overriding (helpful in inheritance)
# 2. duck typing
class Employee:
    def get_designation(self):
        print("designation=Employee")
class Teacher(Employee):
    def get_designation(self):
        print("designation= Teacher")

t1 = Teacher()
t1.get_designation()