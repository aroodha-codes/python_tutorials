# Multiple Inheritence
class Teacher():
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,gpa):
        self.gpa = gpa
    
class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa) #if super given we should not give self
        self.name = name
TA1 = TA(250_00,9.23,"JP")
print(TA1.salary,TA1.gpa,TA1.name)