# Imagine a vending machine that sells various products. 
# The vending machine needs to manage different states such as ready to serve, 
# waiting for product selection, processing payment, and handling out-of-stock situations. 
# Design a system that models the behavior of this vending machine efficiently.

from abc import ABC, abstractmethod

# State interface
class VendingMachineState(ABC):
    @abstractmethod
    def handle_request(self):
        pass

# Concrete states
class ReadyState(VendingMachineState):
    def handle_request(self):
        print("Ready state: Please select a product")

class ProductSelectedState(VendingMachineState):
    def handle_request(self):
        print("Product selected state: Processing payment")

class PaymentPendingState(VendingMachineState):
    def handle_request(self):
        print("Payment pending state: Dispending product")

class OutOfStockState(VendingMachineState):
    def handle_request(self):
        print("Out of stock state: Product unavailable. Please select another product.")

# Context responsible for maintaining the current state of the vending machine and delegating state-specific behavior to the appropriate state object.
class VendingMachineContext:
    def __init__(self):
        self.state = None

    def set_state(self, state: VendingMachineState):
        self.state = state 

    def request(self):
        if self.state:
            self.state.handle_request()
        else:
            print("No state set for the vending machine.")

# Usage
vending_machine = VendingMachineContext()

vending_machine.set_state(ReadyState())
vending_machine.request()

vending_machine.set_state(ProductSelectedState())
vending_machine.request()

vending_machine.set_state(PaymentPendingState())
vending_machine.request()

vending_machine.set_state(OutOfStockState())
vending_machine.request()
