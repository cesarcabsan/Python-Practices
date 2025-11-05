from abc import ABC, abstractmethod

class DataProcessor(ABC):    
    @abstractmethod
    def process_data(self, data):
        pass 