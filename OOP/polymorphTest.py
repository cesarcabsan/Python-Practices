#Polymorphism examples

#With operators
a = 3
b = 5
c = 7
print(a + b * c)

#With strings
str1 = "Bonjour "
str2 = "Monde"
print(str1 + str2)

#With list
list1 = [1,2,3,4,5]
list2 = ["A", "B", "C"]
print(list1+list2)

#multiply string
numstr = 3
thestr = "Python"
print(numstr*thestr)

#With function
mystr = "Programming"
print(len(mystr))

#With classes
class Tiger():
    def sound(self):
        print("The tiger roars")

    def color(self):
        print("The tiger is orange with black strips")

class Lion():
    def sound(self):
        print("The lion roars too")

    def color(self):
        print("The lion is yellow")

tiger_sounds = Tiger()
lion_sounds = Lion()

for animal in (tiger_sounds, lion_sounds):
    animal.sound()
    animal.color()
