class Singleton:
    # This class variable holds the single instance
    _instance = None

    def __new__(cls):
        # The __new__ method is responsible for object creation. It's called every time an instance is created.

        # Check if the instance already exists
        if cls._instance is None:
            # If the instance doesn't exist, create a new instance
            # We use super() to call the __new__ method of the base class (object)
            cls._instance = super(Singleton, cls).__new__(cls)
            print("Singleton is Instantiated.") # This prints only once when the instance is created
        return cls._instance

    # Static method to perform an action on the Singleton instance
    @staticmethod
    def do_something():
        # This method can be called without creating an instance of the class.
        print("Something is Done.")

# Usage example

# First call to create the Singleton instance
s1 = Singleton()
s1.do_something()

# More calls to Singleton will return the same instance
s2= Singleton()
s2.do_something()

s3= Singleton()
s3.do_something()