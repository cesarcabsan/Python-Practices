import math

class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
    
class ScientisticCal(Calculator):
    def sin(self, value):
        return math.sin(value)
    
    def cos(self, value):
        return math.cos(value)
    
    def tan(self, value):
        return math.tan(value)
    
class BusinessCal(Calculator):
    def future_value(self, pv, r, n):
        return pv * (1+r)**n
    def monthly_payment(self, p, r, n):
        return p * (r * (1 + r)**n) / (((1 + r)**n) - 1)

# Objets for the calculators
scical = ScientisticCal()
buscal = BusinessCal()

# Operators inherited from the Basic Calculator
print(scical.add(13, 52))
print(scical.sub(13, 11))
print(buscal.mul(4, 10))
print(buscal.div(33, 2))

# Operators from Scientistic calculator
print(scical.sin(2))
print(scical.cos(3))

#Operators from Business Calculator
print(buscal.future_value(10, 14, 1))
print(buscal.monthly_payment(124, 43, 16))

