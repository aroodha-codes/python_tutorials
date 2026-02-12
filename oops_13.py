#2. Ducktyping
class Employee:
    def get_designation(self):
        print("designation=Employee")
class Teacher():
    def get_designation(self):
        print("designation= Teacher")

t1 = Teacher()
t1.get_designation()

emp1 = Employee()
emp1.get_designation()