#__init__ Method
class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
std1 = Student("Ravi",8.67)
std2 = Student("Vishnu",9.02)
print(std1.name,std1.cgpa)
print(std2.name,std2.cgpa)
