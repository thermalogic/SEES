# -*- coding: utf-8 -*-

print('Yankees rule!')
print('But not in Boston!')
print('Yankees rule,', 'but not in Boston!')

pi = 3
radius = 11
area = pi * (radius**2)
radius = 14

side = 1 #length of sides of a unit square
radius = 1 #radius of a unit circle
#subtract area of unit circle from area of unit square
areaC = pi*radius**2
areaS = side*side
difference = areaS - areaC

x, y = 2, 3
x, y = y, x
print('x =', x)
print('y =', y)

if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')
    
print('Mluvíš anglicky?')
print('क्या आप अंग्रेज़ी बोलते हैं?')

# Square an integer, the hard way
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

#Find a positive integer that is divisible by both 11 and 12
x = 1
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')