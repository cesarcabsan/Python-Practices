# Existing class with incompatible interface
class EuropeanCharger:
    def provide_eu_power(self):
        return "220V power via European plug"

# Expected interface for the new system
class USB_C_Device:
    def charge(self):
        pass

# Adapter to make them compatible
class EUtoUSBCAdapter(USB_C_Device):
    def __init__(self, euro_charger):
        self.euro_charger = euro_charger

    def charge(self):
        power = self.euro_charger.provide_eu_power()
        print(f"Adapter converted: {power} -> Charging device via USB-C")

# Client code

euro_charger = EuropeanCharger()
adapter = EUtoUSBCAdapter(euro_charger)

# Client code uses the common 'charge' method
adapter.charge()
 