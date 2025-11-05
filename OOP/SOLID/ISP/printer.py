from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def printing(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass    

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def printing(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
        def printing(self, document):
            print(f"Printing {document} in color...")
            
        def fax(self, document):
             print(f"Faxing {document}")    
             
        def scan(self, document):
            print(f"Scanning {document}")

bw_photo = OldPrinter()
bw_photo.printing("image")
 
color_photo = NewPrinter()
color_photo.printing("thesis")
color_photo.fax("paper")
color_photo.scan("photo")
