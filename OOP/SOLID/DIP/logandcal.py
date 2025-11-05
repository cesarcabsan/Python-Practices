from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open("log.txt", 'a') as f:
            f.write(message + '\n')

class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result
    
logging = Logger()
logging.log("Calculating")

calculog = Calculator(logging)
calculog.add(10, 52)
