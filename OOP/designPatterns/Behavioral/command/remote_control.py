# Imagine you are tasked with designing a remote control system for various electronic devices in a smart home. 
# The devices include a TV, a stereo, and potentially other appliances. The goal is to create a flexible remote control that can handle different types of commands for each device, 
# such as turning devices on/off, adjusting settings, or changing channels.
from abc import ABC, abstractmethod

## Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete command classes
class TurnOnCommand(Command):
    def __init__(self, device: "Device"):
        self.device = device 

    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device: "Device"):
        self.device = device 

    def execute(self):
        self.device.turn_off() 

class AdjustVolumeCommand(Command):
    def __init__(self, stereo: "Stereo"):
        self.stereo = stereo 

    def execute(self):
        self.stereo.adjust_volume() 

class ChangeChannelCommand(Command):
    def __init__(self, tv: "Television"):
        self.tv = tv 

    def execute(self):
        self.tv.change_channel() 


## Receiver interface
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete receivers
class Television(Device):
    def turn_on(self):
        print("TV is now on")
    
    def turn_off(self):
        print("TV is now off")

    def change_channel(self):
        print("Channel is changed")

class Stereo(Device):
    def turn_on(self):
        print("Stereo is now on")
    
    def turn_off(self):
        print("Stereo is now off")

    def adjust_volume(self):
        print("Volume adjusted")

# Invoker 
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Usage

# Devices
tv = Television()
stereo = Stereo()

# Command objects
turn_on_tv = TurnOnCommand(tv)
turn_off_tv = TurnOffCommand(tv)
adjust_stereo_volume = AdjustVolumeCommand(stereo)
change_tv_channel = ChangeChannelCommand(tv)

# Remote control  
remote = RemoteControl()

# Set and execute commands
remote.set_command(turn_on_tv)
remote.press_button()

remote.set_command(adjust_stereo_volume)
remote.press_button()

remote.set_command(change_tv_channel)
remote.press_button()

remote.set_command(turn_off_tv)
remote.press_button()