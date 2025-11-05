# Consider an example of an online clothing store. You want a specific t-shirt, but it's currently out of stock. 
# You check the site daily to see if it's available. The store offers alerts when the product is back in stock, so you subscribe to receive notifications. 
# This eliminates the need to manually check the store.

# The Observable class defines the interface for objects that can be observed.
class Observable:
    def subscribe(self, observer):
        raise NotImplementedError
    
    def unsubscribe(self, observer):
        raise NotImplementedError

    def notify(self):
        raise NotImplementedError

# Concrete implementation of the Observable class.
class Store(Observable):
    def __init__(self):
        self._message = ""
        self._observers = []

    def set_message(self, message: str):
        self._message = message 
        self.notify() # Notify all observers when the message state is changed

    def subscribe(self, observer):
        self._observers.append(observer)
    
    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._message) # Call update method of observer with the new message 


# The Observer class defines the interface for observers that will react to changes in the observable.
class Observer:
    def update(self, message: str):
        raise NotImplementedError

# Concrete implementation of the Observer class
class User(Observer):
    def __init__(self, observable: Observable):
        self._observable = observable 
        self._observable.subscribe(self) # Subscribe automatically when a new User object is created

    def update(self, message: str):
        print(f"Store update: {message}")


# Usage
store = Store()
user = User(store) # After creation, it observes the Store class

# Alternatively, you could subscribe like this:
#store.subscribe(user)

store.set_message("Shirt is available now") # This will call the update method and log the message
store.unsubscribe(user)
store.set_message("Autumn sale is live now") # This message won't be logged as the user has unsubscribed from the observable


# The observer pattern is a widely used behavioral design pattern. It allows objects to subscribe and receive updates about events happening in the object they are observing.