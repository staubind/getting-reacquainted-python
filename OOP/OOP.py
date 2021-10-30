class Dog():
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = 'Schnauzer', name = 'Gussy')
otherdog = Dog('Bernadoodle', 'Barnaby')
print(mydog.breed, mydog.name)
print(otherdog.breed, otherdog.name)

