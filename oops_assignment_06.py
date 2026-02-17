"""
Concept: Abstraction
Q6.Create an abstract class Employee with an abstract method calculate_salary().
Create subclasses:
• Intern
• FullTimeEmployee
• ContractEmployee
Implement calculate_salary() differently in each subclass.
"""
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass
    
# for intern
class Intern(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calc_salary(self):
        salary = self.hourly_rate * self.hours_worked
        return salary
# full time   
class FullTimeEmployee(Employee):
    def __init__(self,monthly_salary):
        self.monthly_salary = monthly_salary
    def calc_salary(self):
        return self.monthly_salary
    
# part time
class ContractEmployee(Employee):
    def __init__(self,project_rate,projects_completed):
        self.project_rate = project_rate
        self.projects_completed = projects_completed
    def calc_salary(self):
        salary = self.project_rate * self.projects_completed
        return salary

#Testing
i1 = Intern(20, 40)
f1 = FullTimeEmployee(5000)
c1 = ContractEmployee(1000, 3)

print(f"Intern salary: Rs{i1.calc_salary()}")
print(f"Full-time salary: Rs{f1.calc_salary()}")
print(f"Contract salary: Rs{c1.calc_salary()}")