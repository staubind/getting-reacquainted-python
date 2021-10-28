# Flow: 
name = 1
if name:
    print(f'name is: {name}')
name = 0

while True:
    name += 1
    print(name)
    if name == 10:
        break

for i in range(5, -1, -1):
    if i % 2 == 0:
        print(f'i is: {i}')
        continue
    print('hello again')

# function with try/except/finally block
def greater_than_four(num):
    try:
        if num > 4:
            print('yup, it\'s greater than 4.')
    except TypeError:
        print('you didn\'t enter a number')
    finally:
        print('we do this every time, regardless')

greater_than_four(5)
#greater_than_four(input('enter a number'))
print(list(range(4)))

x = list(range(5))
x.pop()
print(x)

x.append('hello')
print(x)
x.insert(1,'')
print(x)
print(x[:2])
print(x.index('hello'))
print(x.remove('hello'))
print(x)
print('-----------------------------------')

import copy
x = [[1,2,3],2,[3,3,3,[3.1,3.1,3.1]]]
y = copy.deepcopy(x)

print(x)
y[0] = 1
print(y)

print('-----------------------------------')
a = 'a'
b = 'b'
c = 'c'
a, b, c = c, b, a # multiple assignment
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')
print('-----------------------------------')

characters = 'It was a bright cold day in April, and the clocks were striking 13'
counts = {}
for char in characters:
    counts.setdefault(char, 0)
    counts[char] += 1
import pprint
pprint.pprint(counts)