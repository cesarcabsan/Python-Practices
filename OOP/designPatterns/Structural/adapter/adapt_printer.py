# Let’s consider a scenario where we have an existing system that uses a LegacyPrinter class with a method named print_document() 
# which we want to adapt into a new system that expects a Printer interface with a method named printing(). 
# We’ll use the Adapter design pattern to make these two interfaces compatible.

# Target interface
class Printer:
    def printing(self):
        raise NotImplementedError

# Adaptee (Class with an incompatible interface)
class LegacyPrinter:
    def print_document(self):
        print("The Legacy Printer is printing a document")

# Adapter (Class that adapts the LegacyPrinter to the Printer interface)
class PrinterAdapter(Printer):
    def __init__(self, legacy_printer: LegacyPrinter):
        self.legacy_printer = legacy_printer

    def printing(self):
        self.legacy_printer.print_document()

# Client code (Code that interacts with the Printer interface)
def client_code(printer: Printer):
    printer.printing()

# Usage
legacy_printer = LegacyPrinter()
adapter = PrinterAdapter(legacy_printer)
client_code(adapter)