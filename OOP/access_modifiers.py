### Public access modifier (accesible from any part of the program)
class MyClass:
    def __init__(self):
        self.my_public_attribute = "I am a public attribute"

    def my_public_method(self):
        print("I am a public method")

## Accessing public members
obj = MyClass()
print(obj.my_public_attribute)
obj.my_public_method()

### Protected access modifier (restricts the access of class members within the class and its subclasses)
class MyBaseClass:
    def __init__(self):
        self._my_protected_attribute = "I am a protected attribute"

    def _my_protected_method(self):
        print("I am a protected method")

class MyDerivedClass(MyBaseClass):
    def __init__(self):
        super().__init__()

    def access_protected_member(self):
        print(self._my_protected_attribute)
        self._my_protected_method()

## Accessing protected members
obj = MyDerivedClass()
obj.access_protected_member()

### Private access modifier (restricts the access of class members to within the class only)
class MyPrivateClass:
    def __init__(self):
        self.__my_private_attribute = "I am a private attribute"

    def __my_private_method(self):
        print("I am a private method")

## Accessing private members (will result in AttributeError)
obj = MyPrivateClass()
# print(obj.__my_private_attribute)
# obj.__my_private_method()
 