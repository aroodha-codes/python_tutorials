"""
Concept: Inheritance
Q5.Create a base class Vehicle with attributes:
• brand
• model
Create two subclasses:
• Car, add attribute seats
• Bike, add attribute engine_cc
"""
class Vehicle: #base class
    def __init__(self,brand,model):
        self.brand= brand
        self.model = model

class Car(Vehicle): #subclass
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats
                
class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc
        
#testing        
c1 = Car("Toyota", "Camry", 5)
b1 = Bike("Honda","CBR",600)
print(f"This {c1.brand} {c1.model} has - {c1.seats} seats")
print(f"This {b1.brand} {b1.model} has - {b1.engine_cc} cc")