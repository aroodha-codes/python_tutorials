""" Design & create an online  store for products(name,price)
Track total products created.
Create a static method to calculate discount
on each product based on a %parameter
"""
class Products:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Products.count += 1
    def get_info(self):#instance method
        print(f"Price of {self.name} is {self.price}")
    @classmethod #class method
    def get_count(cls):
        print(f"The count is:{cls.count}")
    @staticmethod #static method
    def calc_discount(price,discount):
        final_price = price - (discount * price/100)
        print(f"The final price is:{final_price}")
P1 = Products("Laptop",55000)
P2 = Products("S_Pen",5000)
P1.get_info()
P1.calc_discount(P1.price,10)
P2.get_info()
P2.calc_discount(P2.price,10)
Products.get_count()