#Encapsulation
#In python there is no completely private
class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name #public
        self._acc_no = acc_no #protected
        self.__balance = balance #private
# we use the getters and setters to access the private data
    def  get_balance(self): #getter
        return self.__balance
    def set_balance(self,newBalance): #setter
        self.__balance = newBalance
acc1 = BankAccount("Kumar",7895,100_000)
acc1.set_balance(200_000)
print(acc1.name,acc1._acc_no,acc1.get_balance())
# to access the private variable (should not do)
print(acc1.name,acc1._acc_no,acc1._BankAccount__balance)