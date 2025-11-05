# Imagine you are building a remote control system for multiple devices like TVs, DVD players, and audio systems. 
# Each device has different features and commands, and you want to support different types of remote controls (e.g., basic remote, advanced remote). 
# The Bridge Design Pattern can help us create a robust and extensible solution.

# Abstraction
class RemoteControl:
    def __init__(self, device):
        self._device = device

    def toggle_power(self):
        self._device.toggle_power()

    def volume_up(self):
        self._device.volume_up()

    def volume_down(self):
        self._device.volume_down()

# Implementation
class Device:
    def toggle_power(self):
        pass

    def volume_up(self):
        pass

    def volume_down(self):
        pass

# Concrete Implementations for Devices
class TV(Device):
    def toggle_power(self):
        print("TV: Toggling power")

    def volume_up(self):
        print("TV: Volume up")

    def volume_down(self):
        print("TV: Volume down")

class DVDPlayer(Device):
    def toggle_power(self):
        print("DVD Player: Toggling power")

    def volume_up(self):
        print("DVD Player: Volume up")

    def volume_down(self):
        print("DVD Player: Volume down")

# Abstraction and Refined Abstraction
class BasicRemoteControl(RemoteControl):
    def toggle_power(self):
        print("Basic Remote: Press power button")
        super().toggle_power()

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Advanced Remote: Mute button pressed")
        self._device.volume_down()

# Client Code
tv = TV()
dvd_player = DVDPlayer()

basic_remote_tv = BasicRemoteControl(tv)
advanced_remote_dvd = AdvancedRemoteControl(dvd_player)

basic_remote_tv.toggle_power()
basic_remote_tv.volume_up()

advanced_remote_dvd.toggle_power()
advanced_remote_dvd.mute()