"""Concept: Encapsulation
Q3.Create a class Student with private attributes:_name,_roll_no,_marks
Provide getter and setter methods with validation:
• marks cannot be negative
• roll number must be between 1 and 100
• name cannot be empty
"""
class Student:
    def __init__(self,name,roll_no,marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks
    #set name
    def set_name(self,name):
        if name == "":
            print("Empty Name can't be added")
        else:
            self._name = name
     #set roll_no
    def set_roll_no(self,roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Enter the valid roll no")
    # set marks
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Enter the valid Marks(0-100).")
    #get name
    def get_name(self):
        return self._name
    #get roll_no
    def get_roll_no(self):
        return self._roll_no
    #get marks
    def get_marks(self):
        return self._marks
s1 = Student("Prajwal GR",1,97)
print(s1.get_name(),s1.get_roll_no(),s1.get_marks())

#validation
s1.set_marks(79)
print(s1.get_marks())
s1.set_name("")
s1.set_roll_no(150)
s1.set_marks(-10) 