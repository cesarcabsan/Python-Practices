from abc import ABC, abstractmethod

#abstract classes or interfaces
class CustomerInterface(ABC):
    @abstractmethod
    def view_products(self):
        pass

    @abstractmethod
    def add_products_to_cart(self):
        pass

    @abstractmethod
    def place_orders(self):
        pass

class AdminInterface(ABC):
    @abstractmethod
    def manage_products(self):
        pass

    @abstractmethod
    def manage_orders(self):
        pass

    @abstractmethod
    def manage_customers(self):
        pass

# child classes that implement their respective interface
class Customer(CustomerInterface):
    def view_products(self):
        print("Customer is viewing the products to buy")

    def add_products_to_cart(self):
        print("Customer is adding products to the cart")

    def place_orders(self):
        print("Customer is placing an order")
    
class Admin(AdminInterface):
    def manage_products(self):
        print("\nAdmin is managing the products")

    def manage_orders(self):
        print("Admin is managing an order")

    def manage_customers(self):
        print("Admin is managing the customers")

#usage

customer = Customer()
customer.view_products()
customer.add_products_to_cart()
customer.place_orders()

admin = Admin()
admin.manage_products()
admin.manage_orders()
admin.manage_customers()