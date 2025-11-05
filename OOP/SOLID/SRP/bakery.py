class BreadBaker:
    def bake_bread(self):
        print("Baking high quality bread...")
        
class InventoryManager:
    def manage_inventory(self):
        print("Managing inventory... ")
        
class SupplyOrder:
    def order_supplies(self):
        print("Ordering suplies... ")
        
class CustomerService:
    def serveCustomer(self):
        print("Serving costumers... ")
        
class BakeryCleaner:
    def cleanBakery(self):
        print("Cleaning the bakery...")
        
baker = BreadBaker() 
inventory_manager = InventoryManager()  
supply_order = SupplyOrder()  
customer_service= CustomerService() 
cleaner = BakeryCleaner()  

baker.bake_bread()
inventory_manager.manage_inventory()
supply_order.order_supplies()
customer_service.serveCustomer()
cleaner.cleanBakery()