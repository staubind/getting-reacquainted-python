from math import sqrt

def area(d, l): 
    # your code here
    if d <= l:
        return 'Not a rectangle'
    return sqrt(d**2-l**2)*l