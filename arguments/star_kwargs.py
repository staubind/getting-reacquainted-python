# *args for non-keyword args
    # for accepting unknown number of args
    # convention to use args after *
    # a tupple
# **kwargs for keyword args

# example
def myFunc(**kwargs):
    print(type(kwargs))
    for arg in kwargs:
        print('arg is: ', arg)
        print('val is: ', kwargs[arg])
    print(kwargs)
x = 1
y = 2
z = 3

myFunc(x=x,y=y,z=z)