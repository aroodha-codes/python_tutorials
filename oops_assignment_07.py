"""
Concept: Constructor Overloading using Default Parameters
Q7.Create a class Person that allows the constructor to work with:
• name only
• name and age
• name, age and address
Use default parameters to simulate constructor overloading.
"""
class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address
        
#testing
p1 = Person("Alice")
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30, "New York")

print(f"{p1.name}, {p1.age}, {p1.address}")
print(f"{p2.name}, {p2.age}, {p2.address}")
print(f"{p3.name}, {p3.age}, {p3.address}")