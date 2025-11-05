from abc import ABC, abstractmethod
import platform

# File system receiver interface
class FileSystemReceiver(ABC):
    @abstractmethod
    def open_file(self):
        pass
    
    @abstractmethod
    def write_file(self):
        pass
    
    @abstractmethod
    def close_file(self):
        pass
    
# Concrete receivers
class UnixFileSystemReceiver(FileSystemReceiver):
    def open_file(self):
        print("Opening file in Unix OS")
    
    def write_file(self):
        print("Writing file in Unix OS")
    
    def close_file(self):
        print("Closing file in Unix OS")


class WindowsFileSystemReceiver(FileSystemReceiver):
    def open_file(self):
        print("Opening file in Windows OS")
    
    def write_file(self):
        print("Writing file in Windows OS")
    
    def close_file(self):
        print("Closing file in Windows OS")


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 

# Concrete commands
class OpenFileCommand(Command):
    def __init__(self, file_system: FileSystemReceiver):
        self.file_system = file_system

    def execute(self):
        self.file_system.open_file()

class WriteFileCommand(Command):
    def __init__(self, file_system: FileSystemReceiver):
        self.file_system = file_system

    def execute(self):
        self.file_system.write_file()

class CloseFileCommand(Command):
    def __init__(self, file_system: FileSystemReceiver):
        self.file_system = file_system

    def execute(self):
        self.file_system.close_file()

# Invoker class
class FileInvoker:
    def __init__(self, command: Command):
        self.command = command 
    
    def execute(self):
        self.command.execute()

# Utility to detect OS and return appropiate receiver
class FileSystemReceiverUtil:
    @staticmethod
    def get_underlying_file_system():
        os_name = platform.system()
        print(f"Underlying OS is: {os_name}")
        if "Windows" in os_name:
            return WindowsFileSystemReceiver()
        else:
            return UnixFileSystemReceiver()

# Create receiver (Usage)
file_system = FileSystemReceiverUtil.get_underlying_file_system()

# Open file
open_command = OpenFileCommand(file_system)
file = FileInvoker(open_command)
file.execute()

# Write file
write_command = WriteFileCommand(file_system)
file = FileInvoker(write_command)
file.execute()

# Close file
close_command = CloseFileCommand(file_system)
file = FileInvoker(close_command)
file.execute()