from abc import ABC, abstractmethod

# Abstract State
class CoffeeMachineState(ABC):
    def __init__(self, coffee_machine):
        self.coffee_machine = coffee_machine 

    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_coffee(self):
        pass

    @abstractmethod
    def dispense_coffee(self):
        pass

# Concrete classes
class IdleState(CoffeeMachineState):
    def insert_coin(self):
        print("Coin inserted. Please select your coffee...")
        self.coffee_machine.set_state(SelectingState(self.coffee_machine))

    def select_coffee(self):
        print("Insert coin first.")

    def dispense_coffee(self):
        print("Insert coin and select coffee first.")

class SelectingState(CoffeeMachineState):
    def insert_coin(self):
        print("Coin already inserted. Please select your coffee.")
    
    def select_coffee(self):
        print("Coffee selected. Dispensing now...")
        self.coffee_machine.set_state(DispensingState(self.coffee_machine))
    
    def dispense_coffee(self):
        print("Select coffee before dispensing.")

class DispensingState(CoffeeMachineState):
    def insert_coin(self):
        print("Please wait. Dispensing coffee.")
    
    def select_coffee(self):
        print("Already dispensing. Please wait.")
    
    def dispense_coffee(self):
        print("Coffee dispensed. Enjoy!")
        self.coffee_machine.set_state(IdleState(self.coffee_machine))


# Context class
class CoffeeMachine:
    def __init__(self):
        self.state = IdleState(self)

    def set_state(self, state: CoffeeMachineState):
        self.state = state 

    def insert_coin(self):
        self.state.insert_coin()

    def select_coffee(self):
        self.state.select_coffee()

    def dispense_coffee(self):
        self.state.dispense_coffee()

# Usage
coffee_machine = CoffeeMachine()
coffee_machine.select_coffee()      # Invalid: no coin
coffee_machine.insert_coin()        # Valid: moves to SelectingState
coffee_machine.dispense_coffee()    # Invalid: must select coffee
coffee_machine.select_coffee()      # Valid: moves to DispensingState
coffee_machine.insert_coin()        # Invalid: wait for dispensing
coffee_machine.dispense_coffee()    # Valid: back to IdleState

