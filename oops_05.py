#Instance Method and class method Example
class Laptop:
    storage_type = "SSD"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage
        #class method
    """@classmethod is a decorator because it changes a normal function into a method that
    automatically receives the class as its first argument instead of an object."""
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type is : {cls.storage_type}")
        #instance method
    def get_info(self):
        print(f"The Laptop has {self.ram} RAM and {self.storage} {self.storage_type}")
    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price/100)
        print(f"The discounted price is:{final_price}")
l1 = Laptop("16GB","512")
l2 = Laptop("8GB","256")
l1.get_info()              
l2.get_info()
l1.get_storage_type()
l1.calc_discount(40_000,12)