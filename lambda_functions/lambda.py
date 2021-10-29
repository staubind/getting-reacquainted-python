# problems found here: https://www.w3resource.com/python-exercises/lambda/index.php

# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result

add_fifteen = lambda x: x + 15

print(add_fifteen(5))

multiply = lambda x, y: x * y

print(multiply(3,5))

# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. Go to the editor
import random
print(random.randrange(1, 50))
mult_random = lambda x: x * random.randrange(1,100)

# Write a Python program to sort a list of tuples using Lambda.
input = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
input.sort(key = lambda x: x[1]) # cool! I found this on the internet, but looks like sort can take a function by which to sort

# 4. Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
input = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
input.sort(key=lambda x: x['color'])
print(input)

# 5. Write a Python program to filter a list of integers using Lambda. Go to the editor
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# get evens
evens = list(filter(lambda x: x % 2 == 0, input))
print(evens)

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = list(map(lambda x: x**2, input))
print(output)

# 8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor
import datetime
date_time = lambda x: f'{x.year}-{x.month}-{x.day} {x.hour}:{x.minute}:{x.second}'
print(date_time(datetime.datetime.now()))

# 9. Write a Python program to check whether a given string is number or not using Lambda. Go to the editor
isNumber = lambda x: x.replace('.','').isdigit()
print(isNumber('abcde123'))
print(isNumber('.5')) 
print(isNumber('5'))
# had to get some help on the second case. Interesting though! learned about replace and isdigit! awesome.

# 10. Write a Python program to create Fibonacci series upto n using Lambda. Go to the editor
# ???  apparently this:
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0,1]) 