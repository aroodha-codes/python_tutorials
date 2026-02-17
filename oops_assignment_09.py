"""
Concept: Multiple Inheritance
Q9.Create the classes:
• Herbivore
• Carnivore
• Omnivore
Each should have some attributes and methods.
Then create a class Bear that inherits from all three classes to demonstrate multiple inheritance.
"""
class Herbivore:
    def __init__(self):
        self.diet_type = "Plants"
    def eat_plants(self):
        print("Eat Plants as food.")
class Carnivore:
    def __init__(self):
        self.diet_type = "Prey"
    def eat_meat(self):
        print("Eats meat as food.")
class Omnivore:
    def __init__(self):
        self.diet_type = "Both"
    def flexible(self):
        print("Eats both plants and animals.")
#bear class  
class Bear(Herbivore,Carnivore,Omnivore):
        pass
    
# Testing
b = Bear()
h = Herbivore()
print(h.diet_type)
b.eat_plants()   # From Herbivore
b.eat_meat()     # From Carnivore
b.flexible()     # From Omnivore
print("Bear inherited methods from all three classes!")