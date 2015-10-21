# Page 9

print('Yankees rule!')
print('But not in Boston!')
print('Yankees rule,', 'but not in Boston!')

#Page 11
pi = 3
radius = 11
area = pi * (radius**2)
radius = 14

#Page 13
x, y = 2, 3
x, y = y, x
print('x =', x)
print('y =', y)

#Page 15
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

x = 12
y = 5
z = 13
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

#Page 19
x = 3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))
