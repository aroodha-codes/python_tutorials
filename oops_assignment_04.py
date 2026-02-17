"""
Concept: Function Overriding
Q4.Create a class Shape with a method area().
Create subclasses:
• Circle
• Rectangle
• Triangle
Override the area() method in each subclass.
"""
import math
class Shape:
    def area(self):
        print("Undefined shape.")
# circle     
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = math.pi * self.radius ** 2
        return area
    
#Rectangle
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        return area
    
#Triangle
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        area = 0.5 * self.base *self.height
        return area
    
#testing
shapes = [Circle(5), Rectangle(4, 6), Triangle(10, 8)]
for shape in shapes:
    print(f"{shape.area():.2f}")
    
c1 = Circle(5)
r1 = Rectangle(4, 6)
t1 = Triangle(10, 8)
print(f"Circle area: {c1.area():.2f}")      # ~78.54
print(f"Rectangle area: {r1.area()}")   # 24
print(f"Triangle area: {t1.area()}")    # 40.0