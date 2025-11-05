from abc import ABC, abstractmethod

# Interface for the components
class IComponent(ABC):
    @abstractmethod
    def notify(self, msg):
        pass
    
    @abstractmethod
    def receive(self, msg):
        pass

# Concrete implementation of the Component class that interacts through the Mediator
class Component(IComponent):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name
        
    # Notify the mediator to broadcast a message to other components
    def notify(self, message):
        print(f"{self.name} >>> out >>> {message}")
        self.mediator.notify(message, self) # Mediator notifies other components
        
    # Receive a message from other components
    def receive(self, message):
        print(f"{self.name} >>> in >>> {message}")
 
# Mediator class coordinates communication between components
class Mediator:
    def __init__(self):
        self.components = [] # List to store components
        
    # Add a component to the mediator's list of components
    def add(self, component):
        self.components.append(component)
        
    # Notify all components except the one that sent the message
    def notify(self, message, component):
        for _component in self.components:
            if _component != component: # Avoid notifying the sender
                _component.receive(message) # Send the message to other components
            
# Usage
mediator = Mediator()
component1 = Component(mediator, "Component1")
component2 = Component(mediator, "Component2")
component3 = Component(mediator, "Component3")

mediator.add(component1)
mediator.add(component2)
mediator.add(component3)

# One of the components sends a message via the mediator, which broadcasts it to other components
component1.notify("data")