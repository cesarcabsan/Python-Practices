class Duck:
    def swim_fly(self):
        print("Quack, fly and swim")

class Goose:
    def swim_fly(self):
        print("Honk, fly and swim")

class Ostrich():
    def walk_run(self):
        print("Swim and slide")

for obj in Duck(), Goose(), Ostrich():
    obj.swim_fly()
#Duck typing prioritizes functionality over specific data types for example,
#in these three classes, we can see that Duck and Goose can swim and fly, but Ostrich can't, 
#therefore the ostrich class can't make use of the swim_fly method.


