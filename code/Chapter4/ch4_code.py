# Page 34, figure 4.1
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

# Page 35


def max(x, y):
    if x > y:
        return x
    else:
        return y

# Page 36, Figure 4.2


def printName(firstName, lastName, reverse):
   if reverse:
      print(lastName + ', ' + firstName)
   else:
      print(firstName, lastName)

# Page 36
printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', False)
printName('Olga', 'Puchmajerova', reverse=False)
printName('Olga', lastName='Puchmajerova', reverse=False)
printName(lastName='Puchmajerova', firstName='Olga', reverse=False)

# Page 37

printName('Olga', lastName='Puchmajerova', False)


def printName(firstName, lastName, reverse=False):
   if reverse:
      print(lastName + ', ' + firstName)
   else:
      print(firstName, lastName)

printName('Olga', 'Puchmajerova')
printName('Olga', 'Puchmajerova', True)
printName('Olga', 'Puchmajerova', reverse=True)

# 4.1.3 Scoping


def f(x):  # name x used as formal parameter
    y = 1
    x = x + y
    print('x =', x)
    return x

x = 3
y = 2
z = f(x)  # value of x used as actual parameter
print('z =', z)
print('x =', x)
print('y =', y)

# Page 38, Figure 4.3


def f(x):
   def g():
      x = 'abc'
      print('x =', x)

   def h():
      z = x
      print('z =', z)
   x = x + 1
   print('x =', x)
   h()
   g()
   print('x =', x)
   return g

x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()

# Page 40


def f():
   print(x)


def g():
   print(x)
   x = 1

x = 3
f()
x = 3
g()

# Page 42, Figure 4.5


def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    if x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ' + str(x) +
                  ' and power = ' + str(power))
            result = findRoot(x, power, epsilon)
            if result == None:
                print('   No root')
            else:
                print('   ', result**power, '~=', x)

# Page 45, Figure 4.6


def factI(n):
   """Assumes that n is an int > 0
      Returns n!"""
   result = 1
   while n > 1:
      result = result * n
      n -= 1
   return result


def factR(n):
   """Assumes that n is an int > 0
      Returns n!"""
   if n == 1:
      return n
   else:
       return n * factR(n - 1)

# Page 47, Figure 4.7


def fib(n):
    """Assumes n an int >= 0
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def testFib(n):
    for i in range(n + 1):
        print('fib of', i, '=', fib(i))

# Page 48, Figure 4.8


def isPalindrome(s):
    """Assumes s is a str
      Returns True if s is a palindrome; False otherwise.
        Punctuation marks, blanks, and capitalization are
        ignored."""

    def toChars(s):
      s = s.lower()
      letters = ''
      for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
      return letters

    def isPal(s):
      print('  isPal called with', s)
      if len(s) <= 1:
         print('  About to return True from base case')
         return True
      else:
         answer = s[0] == s[-1] and isPal(s[1:-1])
         print('  About to return', answer, 'for', s)
         return answer

   return isPal(toChars(s))

# page 49, Figure 4.9
def isPalindrome(s):
   """Assumes s is a str
      Returns True if s is a palindrome; False otherwise.
        Punctuation marks, blanks, and capitalization are
        ignored."""
   
   def toChars(s):
      s = s.lower()
      letters = ''
      for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
      return letters

   def isPal(s):
      print('  isPal called with', s)
      if len(s) <= 1:
         print('  About to return True from base case')
         return True
      else:
         answer = s[0] == s[-1] and isPal(s[1:-1])
         print( '  About to return', answer, 'for', s)
         return answer
         
   return isPal(toChars(s))

def testIsPalindrome():
   print('Try dogGod')
   print( isPalindrome('dogGod'))
   print('Try doGood')
   print (isPalindrome('doGood'))

# Page 51, Figure 4.10
def fib(x):
    """Assumes x an int >= 0
       Returns Fibonacci of x"""
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times.')

# Page 52, See circle.py

# Page 52
import circle
print( circle.pi)
print( circle.area(3))
print( circle.circumference(3))
print( circle.sphereSurface(3))

from circle import *
print(pi)
print(circle.pi)

# Page 53
nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

# Page 54
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

nameHandle = open('kids', 'w')
nameHandle.write('Michael\n')
nameHandle.write('Mark\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()

nameHandle = open('kids', 'a')
nameHandle.write('David\n')
nameHandle.write('Andrea\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line[:-1])
nameHandle.close()
