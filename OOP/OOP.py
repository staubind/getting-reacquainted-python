class Dog():
    # class object attribute
        # all instance of dog Classes
    species = 'mammal'

    # for particular instance of a dog
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed = 'Schnauzer', name = 'Gussy')
otherdog = Dog('Bernadoodle', 'Barnaby')
print(mydog.breed, mydog.name, mydog.species)
print(otherdog.breed, otherdog.name, otherdog.species)

class Circle():
    # class object attribute
    pi = 3.14

    def area(self):
        # must use self.radius otherwise it doesn't know which one you want
        # use circle.pi because the circle class holds the pi value we want to use
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

    # instance initialization
    def __init__(self, radius=1):
        self.radius = radius

myc = Circle()
print(myc.pi)
print(myc.area) # this is the area method, not the result of that function
print(myc.area())
myc = Circle(3)
print(myc.radius)
myc.set_radius(1)
print(myc.radius)
