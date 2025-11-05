from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of {amount:.2f}")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of {amount:.2f}")

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount: float):
        payment_method.process_payment(amount)

processor = PaymentProcessor()

credit_card = CreditCardPayment()
processor.process_payment(credit_card, 100.0)

paypal = PayPalPayment()
processor.process_payment(paypal, 50.0)



