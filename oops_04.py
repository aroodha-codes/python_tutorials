#Attributes : Class & Instance
class Student:
    college_name = "Apna College"#class
    def __init__(self,name,gpa):
        self.name = name  #Instance
        self.gpa = gpa
s1 = Student("Ankith",19)
print(s1.college_name,s1.name,s1.gpa)