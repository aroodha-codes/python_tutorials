#multilevel inheritence
class Employee:
    start_time = "10:00 AM"
    end_time = "4:00 PM"
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject
class Accounts(Teacher):
    def __init__(self,salary,subject):
        super().__init__(subject)
        self.salary = salary
emp1 = Accounts(250_000,"Kumar")
print(emp1.subject,emp1.salary,emp1.start_time,emp1.end_time)