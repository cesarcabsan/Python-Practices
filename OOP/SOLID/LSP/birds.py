from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Duck(Bird, FlyingBird):
    def eat(self):
        print("Duck is eating")
        
    def sleep(self):
        print("Duck is sleeping")
  
    def fly(self):
        print("Duck is flying")

class Ostrich(Bird):
    def eat(self):
        print("Ostrich is eating")
        
    def sleep(self):
        print("Ostrich is sleeping")

class Eagle(Bird, FlyingBird):
    def eat(self):
        print("Eagle is eating")
        
    def sleep(self):
        print("Eagle is sleeping")
  
    def fly(self):
        print("Eagle is flying")

# Function that accepts any Bird type
def bird_actions(bird: Bird):
    bird.eat()
    bird.sleep()
    # Only call the fly method if the bird can fly
    if isinstance(bird, FlyingBird):
        bird.fly()

duck = Duck()
bird_actions(duck)

ostrich = Ostrich()
bird_actions(ostrich)

eagle = Eagle()
bird_actions(eagle)