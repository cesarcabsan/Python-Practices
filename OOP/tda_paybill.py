# Tell Don´t Ask Principle (TDA): Tell an object to perform an action rather than asking for information and taking action on behalf of the object.

class Customer:
    def __init__(self):
        # The Customer object is responsible for initializing and maintaining its wallet state.
        self.wallet = {"cash": 100}
        
    def pay(self, payment_amount):
        # Telling the Customer to pay a certain amount. It knows how to handle the payment
        # internally by decreasing its own cash.
        self.wallet["cash"] -= payment_amount
        
class PayBillService:
    def handle(self, payment_amount):
        # Telling the PayBillService to handle the payment, but it doesn't ask for the customer's wallet state.
        customer = Customer()
        customer.pay(payment_amount)
        # The service doesn't directly manipulate the customer's cash. It simply tells the Customer to pay.
        # After the payment, it tells the Customer to handle the payment internally and display the result.
        print(f"Remaining cash after payment: {customer.wallet['cash']}")

#Usage
pay_bill_service = PayBillService()
pay_bill_service.handle(10)