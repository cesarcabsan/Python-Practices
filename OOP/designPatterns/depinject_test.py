### Dependency Injection involves supplying the dependencies of a class from the outside rather than creating them within the class.

## Example with Constructor Injection
# The Constructor injection passes dependencies to a class through its constructor.
class LightBulb:
    def turn_on(self):
        print("Lightbulb is ON")

# Applying the Constructor Injection
class Switch:
    # Constructor accepts a device (could be any object with a `turn_on` method)
    def __init__(self, device):
        self.device = device

    def press(self):
        self.device.turn_on() # Call the `turn_on` method of the injected device

# Usage
bulb = LightBulb()
switch_button = Switch(bulb) # Create an instance of Switch, injecting the LightBulb object as the dependency
switch_button.press()


## Example with Method Injection 
# The method injection passes dependencies to an specific method of an object, instead of to the object's constructor or properties.
class UserManager:
    def authenticate(self, username: str, password: str, auth_service):
        # Use the injected authentication service
        auth_service.authenticate(username, password)
        # Authentication logic (you can add more logic here if needed)
    
    def update_profile(self, user, profile_service):
        # Use the injected profile service
        profile_service.update_profile(user)
        # Profile update logic (you can add more logic here if needed)

# Example of an AuthenticationService
class AuthenticationService:
    def authenticate(self, username: str, password: str):
        print(f"Authenticating user {username} with password {password}")
        # Authentication logic here
        
# Example of a ProfileService
class ProfileService:
    def update_profile(self, user):
        print(f"Updating profile for user {user}")
        # Profile update logic here

# Usage
user_manager = UserManager()
auth_service = AuthenticationService()  # This could be any service that implements 'authenticate'
profile_service = ProfileService()  # This could be any service that implements 'update_profile'

# Authenticating the user
user_manager.authenticate(username="user", password="pass", auth_service=auth_service)

# Updating the user profile
user_manager.update_profile(user="user", profile_service=profile_service)

