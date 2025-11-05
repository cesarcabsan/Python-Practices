from abc import ABC, abstractmethod
#this is an abstract method, which hides complex details,
class RemoteControlInt(ABC): 
    @abstractmethod
    def change_channel(self, channel_number: int):
        pass
    
    @abstractmethod
    def volume_adjust(self, volume_level: int):
        pass

    @abstractmethod
    def access_streaming_service(self, service_name: int):
        pass

class TvRemote(RemoteControlInt):
    def change_channel(self, channel_number):
        print(f"Changing the channel to {channel_number}")

    def volume_adjust(self, volume_level):   
        if volume_level > 100:
            print("Max volume is 100, cant go higher than that. Setting to 100.")
        elif volume_level < 0:
            print("The volume cant be negative. Setting to 0.")
        else:
            print(f"Setting volume to {volume_level}...")

    def access_streaming_service(self, service_name):
        print(f"Accesing streaming service {service_name}")

remote = TvRemote()
remote.change_channel(149)
remote.volume_adjust(-11)
remote.volume_adjust(101)
remote.volume_adjust(60)

remote.access_streaming_service("Amazon Prime")

 