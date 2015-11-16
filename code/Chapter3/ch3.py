# Page 21, Figure 3.1
# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)

# Page 23
imax = int(input('Enter a postive integer: '))
i = 0
while i < imax:
    i = i + 1
print(i)

# Page 24
x = 4
for i in range(0, x):
    print(i)

x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x = 2

# Page 25, Figure 3.2
# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
for ans in range(0, abs(x) + 1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)

# Page 25
total = 0
for c in '123456789':
    total = total + int(c)
print(total)

# Page 26, Figure 3.3
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is close to square root of', x)

# Page 28, Figure 3.4
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

# Page 29
x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')

# Page 33, Figure 3.5
# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = 24.0
guess = k / 2.0
while abs(guess * guess - k) >= epsilon:
    guess = guess - (((guess**2) - k) / (2 * guess))
print('Square root of', k, 'is about', guess)
