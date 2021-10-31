s = "GLOBAL VARIABLE!"

def func():
    global s # use global keyword to grab global
    mylocal = 10
    print(locals()) # returns a dict of local vars
    print(globals())
    print(globals()['s'])
    s = 50
    print(s)
func()
print(s)


def hello(name="Jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"
    
    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"
    
    if name == 'jose':
        return greet
    else:
        return welcome

x = hello()
print(x())