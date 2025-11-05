# Product
class Computer:
    def __init__(self):
        self.cpu = " "
        self.ram = " "
        self.storage = " "

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_storage(self, storage):
        self.storage = storage 

    def display_info(self):
        print(f"Computer Configuration\nCPU: {self.cpu}\nRAM: {self.ram}\nStorage: {self.storage}\n")

# Builder interfaces
class Builder:
    def build_cpu(self):
        raise NotImplementedError

    def build_ram(self):
        raise NotImplementedError

    def build_storage(self):
        raise NotImplementedError
    
    def get_result(self):
        raise NotImplementedError


# Concrete builder
class GamingComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.set_cpu("Gaming CPU")

    def build_ram(self):
        self.computer.set_ram("16GB DDR4")

    def build_storage(self):
        self.computer.set_storage("1TB SSD")

    def get_result(self):
        return self.computer 
    
# Director
class ComputerDirector:
    def construct(self, builder: Builder):
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()

# Client Usage
gaming_builder = GamingComputerBuilder()
director = ComputerDirector()

director.construct(gaming_builder)
gaming_computer = gaming_builder.get_result()

gaming_computer.display_info()
