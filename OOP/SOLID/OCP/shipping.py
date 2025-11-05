from abc import ABC, abstractmethod

class ShippingMethod(ABC):
    @abstractmethod
    def calculate(self, order):
        pass

class Order:
    def __init__(self, items, shipping_method: ShippingMethod):
        self.items = items
        self.shipping_method = shipping_method

class StandardShipping(ShippingMethod):
    def calculate(self, order: Order):
        return sum(item['price'] for item in order.items) * 0.1

class ExpressShipping(ShippingMethod):
    def calculate(self, order: Order):
        return sum(item['price'] for item in order.items) * 0.2

class OvernightShipping(ShippingMethod):
    def calculate(self, order: Order):
        return sum(item['price'] for item in order.items) * 0.3

class ShippingCalculator:
    def calculate_shipping(self, order: Order):
        return order.shipping_method.calculate(order)
    
# Usage  
calculator = ShippingCalculator()

standard_shipping = StandardShipping()
order = Order(items=[{'price': 100}, {'price': 200}], shipping_method=standard_shipping)
print(calculator.calculate_shipping(order))   

express_shipping = ExpressShipping()
order_express = Order(items=[{'price': 100}, {'price': 200}], shipping_method=express_shipping)
print(calculator.calculate_shipping(order_express))   

overnight_shipping = OvernightShipping()
order_overnight = Order(items=[{'price': 100}, {'price': 200}], shipping_method=overnight_shipping)
print(calculator.calculate_shipping(order_overnight))   
 

