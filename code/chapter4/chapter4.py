# -*- coding: utf-8 -*-

#Figure 4.1
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

#Figure 4.2
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

#Figure 4.3 contains no code

#Figure 4.4
def findRoot(x, power, epsilon):
    """Assumes x and epsilon int or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    if x < 0 and power%2 == 0: #Negative number has no even-powered 
                               #roots
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print('Testing x =', str(x), 'and power = ', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('   No root')
            else:
                print('   ', result**power, '~=', x)

#Figure 4.5
def factI(n):
   """Assumes n an int > 0
      Returns n!"""
   result = 1
   while n > 1:
      result = result * n
      n -= 1
   return result

def factR(n):
   """Assumes n an int > 0
      Returns n!"""
   if n == 1:
       return n
   else:
       return n*factR(n - 1)
       
#Figure 4.6 has no code

#Figure 4.7
def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))

#Figure 4.8
def isPalindrome(s):
   """Assumes s is a str
      Returns True if letters in s form a palindrome; False
        otherwise. Non-letters and capitalization are ignored."""
   
   def toChars(s):
      s = s.lower()
      letters = ''
      for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
      return letters

   def isPal(s):
      if len(s) <= 1:
        return True
      else:
        return s[0] == s[-1] and isPal(s[1:-1])
         
   return isPal(toChars(s))

#Figure 4.9
def isPalindrome(s):
   """Assumes s is a str
      Returns True if s is a palindrome; False otherwise.
       Punctuation marks, blanks, and capitalization are ignored."""
   
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

def testIsPalindrome():
   print('Try dogGod')
   print(isPalindrome('dogGod'))
   print('Try doGood')
   print(isPalindrome('doGood'))

testIsPalindrome()

#Figure 4.10
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

#Figure 4.11
pi = 3.14159

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

def sphereSurface(radius):
    return 4.0*area(radius)

def sphereVolume(radius):
    return (4.0/3.0)*pi*(radius**3)
