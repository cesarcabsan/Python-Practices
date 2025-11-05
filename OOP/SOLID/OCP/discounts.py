from abc import ABC, abstractmethod

class DiscountInterface(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass
    
class PercentageDiscount(DiscountInterface):
    def __init__(self, percentage):
        self.percentage = percentage
        
    def apply_discount(self, price):
        return price - (price * self.percentage / 100)
        
class FixedAmountDiscount(DiscountInterface):
    def __init__(self, amount):
        self.amount = amount
        
    def apply_discount(self, price):
        return price - self.amount 

# Discount processor to apply the discount types accordingly
class DiscountProcessor:
    def apply_discount(self, price, discount: DiscountInterface):
        return discount.apply_discount(price)

## Usage
price = 150

percentage_discount = PercentageDiscount(25)
fixed_discount = FixedAmountDiscount(30)

discount_processor = DiscountProcessor()

print(f"Price after percentage discount: {discount_processor.apply_discount(price, percentage_discount)}")
print(f"Price after fixed discount: {discount_processor.apply_discount(price, fixed_discount)}")



 