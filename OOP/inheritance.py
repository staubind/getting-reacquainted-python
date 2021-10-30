# INHERITANCE
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')
    
    def whoAmI(self):
        print('ANIMAL')

    def eat(self):
        print('EATING')

mya = Animal()
mya.whoAmI()
mya.eat()

class Dog(Animal):

    def __init__(self):
        print('DOG CREATED')

    def bark(self):
        print('WOOF')
    
    def eat(self):
        print('dog is eating')

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
# SPECIAL METHODS