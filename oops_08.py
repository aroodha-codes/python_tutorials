# Inheritence
class Employee:
    start_time = "10:00 AM"
    end_time = "4:00 PM"
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject
t1 = Teacher("English")
print(t1.subject,t1.start_time,t1.end_time)