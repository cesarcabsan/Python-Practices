from abc import ABC, abstractmethod

# Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategy classes
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} with credit card")
        
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
            print(f"Paid {amount} with PayPal")
        
class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using bank transfer")
        
# Context class
class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
        
    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
        
    def make_payment(self, amount):
        self.payment_strategy.pay(amount)
        
# Usage
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()

payment_context = PaymentContext(credit_card)
payment_context.make_payment(100)

# Change payment strategy
payment_context.set_payment_strategy(paypal)
payment_context.make_payment(50)

payment_context.set_payment_strategy(bank_transfer)
payment_context.make_payment(200)