# Suppose you are developing an e-commerce application where customers can place orders, make payments, and receive notifications. 
# The process of handling an order involves multiple subsystems like inventory management, payment processing, and notification services. Directly interacting with these subsystems from the client code can make the application complex and difficult to maintain.

class Inventory:
    def check_stock(self, product_id):
        print(f"Checking stock for product {product_id}")
        # Simulate stock check
        return True

    def update_stock(self, product_id, quantity):
        print(f"Updating stock for product {product_id} by {quantity}")

class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        # Simulate payment processing
        return True

class Notification:
    def send_confirmation(self, order_id):
        print(f"Sending confirmation for order {order_id}")

# Class for providing a simplified interface for placing orders by interacting with the Inventory, Payment, and Notification subsystems.
class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.notification = Notification()

    def place_order(self, product_id, quantity, amount):
        if self.inventory.check_stock(product_id):
            if self.payment.process_payment(amount):
                self.inventory.update_stock(product_id, -quantity)
                self.notification.send_confirmation(product_id)
                print("Order placed successfully")
            else:
                print("Payment processing failed")
        else:
            print("Product is out of stock")

# Client code
facade = OrderFacade()
facade.place_order(product_id=1, quantity=1, amount=100)


# By using the Facade Method Design Pattern, the complexities of handling orders in an e-commerce system are hidden behind the 
# OrderFacade class, making the client code cleaner and easier to manage.