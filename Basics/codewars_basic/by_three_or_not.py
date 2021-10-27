# prompt:

# A trick I learned in elementary school to determine whether or not a number was divisible by three is to add all of the integers in the number together and to divide the resulting sum by three. If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

# Given a series of digits as a string, determine if the number represented by the string is divisible by three.

# You can expect all test case arguments to be strings representing values greater than 0.

# Example:

# "123"      -> true
# "8409"     -> true
# "100853"   -> false
# "33333333" -> true
# "7"        -> false
# Try to avoid using the % (modulo) operator.

from functools import reduce

def divisible_by_three(st): 
    # just to see if I could do it a different way
    # sum = reduce(lambda x, y: int(x) + int(y), list(st))
    sum = 0
    for num in st:
        sum += int(num)
    # deal with divisibility
    while sum > 2:
        sum -= 3
        if sum == 0:
            return True
    return False


print(divisible_by_three('123'))