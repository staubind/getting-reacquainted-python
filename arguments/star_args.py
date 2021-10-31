# *args for non-keyword args
    # for accepting unknown number of args
    # convention to use args after *
    # a tupple
# **kwargs for keyword args

# example
def myFunc(*args):
    print(type(args))
    for arg in args:
        print(arg)

myFunc(1,2,3,4,5,6,7,7,8,9)