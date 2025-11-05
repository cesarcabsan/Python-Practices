class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance


cesarAccount = BankAccount()
cesarAccount.deposit(130)
cesarAccount.withdraw(50)
print(cesarAccount.get_balance())

'''
Encapsulation focuses on bundling data and methods within a class, 
restricting direct access to the internal state of an object, ensuring 
data protection and enabling controlled access to the object's attributes.
The encapsulation uses (_).
'''

#use the setter
class Artifact:
    def __init__(self):
        self.__maxprice = 950
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):  
        self.__maxprice = price

ar = Artifact()
ar.sell()

ar.__maxprice = 1020 #the sell method cannot change the value, because self.__maxprice is a private variable.
ar.sell()

ar.setMaxPrice(1020) #To change the value, we use the setter function.
ar.sell()
