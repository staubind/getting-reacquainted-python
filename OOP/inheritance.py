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
mylist = [1,2,3]
print(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book('Python', 'jose', 200)
print(b) # w/o the __str__ method defined, it just prints out the location in memory

Book.__str__ = lambda x: 'hello' # one way, probably not pythonic.
print(b)
# probably prefer this:
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('a book is destroyed')


b = Book('Python', 'jose', 200)
print(b)
print(len(b)) # returns an object because we don't have have __len__ method
del b

