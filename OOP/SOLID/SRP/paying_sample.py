class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

class PaymentProcesor:
    def pay(self, order: Order, security_code):
        print("Processing payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)

processor = PaymentProcesor()
processor.pay(order, "0372846")
print(order.status)
