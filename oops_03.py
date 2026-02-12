#Types of constructor : default & Parameterized  
#Default
class Student:
    def __init__(self):
        print("Runs automatically when object is called.")
std1 = Student()
#Parameterized
class Std:
    def __init__(self,name,age):
        self.name = name
        self.age = age
std1 = Std("Rahul",21)
std2 = Std("Abhi",22)
print(std1.name,std1.age)
print(std2.name,std2.age)

