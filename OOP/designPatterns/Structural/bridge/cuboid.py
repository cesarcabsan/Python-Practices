class ProduceAPI1:
    # implementation specific Abstractions
    def produce_cuboid(self, length, breadth, height):
        print(f"API1 is producing cuboid with length = {length}, Breadth = {breadth}, and Height = {height}")

class ProduceAPI2:
    # implementation specific Abstractions
    def produce_cuboid(self, length, breadth, height):
        print(f"API2 is producing cuboid with length = {length}, Breadth = {breadth}, and Height = {height}")


class Cuboid:
    def __init__(self, length, breadth, height, producingAPI):
        """ Initialize the necessary attributes
            Implementation independent Abstraction """
        self._length = length 
        self._breadth = breadth
        self._height = height
        self._producingAPI = producingAPI


    def produce(self):
        # implementation specific Abstractions
        self._producingAPI.produce_cuboid(self._length, self._breadth, self._height) 

    def expand(self, times):
        # implementation independent Abstractions
        self._length = self._length * times 
        self._breadth = self._breadth * times
        self._height = self._height * times

# Code Usage
cuboid1 = Cuboid(3,6,9, ProduceAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19,18,17, ProduceAPI2())
cuboid2.produce()