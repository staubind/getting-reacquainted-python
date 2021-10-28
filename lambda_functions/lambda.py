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


