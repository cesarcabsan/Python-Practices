# Consider a scenario where you have a weather monitoring system. Different parts of your application need to be updated when the weather conditions change.
from abc import ABC, abstractmethod 

# Interfaces
class Observer(ABC):
    @abstractmethod
    def update(self, weather):
        pass
        
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass
        
    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass
        
    @abstractmethod
    def notify_observers(self):
        pass
        
# Concrete Subject 
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._weather = None
        
    def add_observer(self, observer: Observer):
        self._observers.append(observer)
        
    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)
        
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._weather)
            
    def set_weather(self, new_weather):
        self._weather = new_weather
        self.notify_observers()

# Concrete Observers
class PhoneDisplay(Observer):
    def __init__(self):
        self._weather = None
        
    def update(self, weather):
        self._weather = weather
        self.display()
        
    def display(self):
        print(f"Phone Display: Weather updated - {self._weather}")

class TvDisplay(Observer):
    def __init__(self):
        self._weather = None
        
    def update(self, weather):
        self._weather = weather
        self.display()
        
    def display(self):
        print(f"TV Display: Weather updated - {self._weather}")
    
# Usage
weather_station = WeatherStation()

phone_display = PhoneDisplay()
tv_display = TvDisplay()

weather_station.add_observer(phone_display)
weather_station.add_observer(tv_display)

weather_station.set_weather("Sunny")
weather_station.remove_observer(phone_display)
weather_station.set_weather("Rainy")