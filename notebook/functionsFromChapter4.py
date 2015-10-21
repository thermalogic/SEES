#Page 45, Figure 4.6
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
       return n*factR(n - 1)

#Page 47, Figure 4.7
def fib(n):
    """Assumes n an int >= 0
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

##
###Page 48, Figure 4.8
##def isPalindrome(s):
##   """Assumes s is a str
##      Returns True if s is a palindrome; False otherwise.
##        Punctuation marks, blanks, and capitalization are
##        ignored."""
##   
##   def toChars(s):
##      s = s.lower()
##      letters = ''
##      for c in s:
##        if c in 'abcdefghijklmnopqrstuvwxyz':
##            letters = letters + c
##      return letters
##
##   def isPal(s):
##      print '  isPal called with', s
##      if len(s) <= 1:
##         print '  About to return True from base case'
##         return True
##      else:
##         answer = s[0] == s[-1] and isPal(s[1:-1])
##         print '  About to return', answer, 'for', s
##         return answer
##         
##   return isPal(toChars(s))
##
###page 49, Figure 4.9
##def isPalindrome(s):
##   """Assumes s is a str
##      Returns True if s is a palindrome; False otherwise.
##        Punctuation marks, blanks, and capitalization are
##        ignored."""
##   
##   def toChars(s):
##      s = s.lower()
##      letters = ''
##      for c in s:
##        if c in 'abcdefghijklmnopqrstuvwxyz':
##            letters = letters + c
##      return letters
##
##   def isPal(s):
##      print '  isPal called with', s
##      if len(s) <= 1:
##         print '  About to return True from base case'
##         return True
##      else:
##         answer = s[0] == s[-1] and isPal(s[1:-1])
##         print '  About to return', answer, 'for', s
##         return answer
##         
##   return isPal(toChars(s))
##
##def testIsPalindrome():
##   print 'Try dogGod'
##   print isPalindrome('dogGod')
##   print 'Try doGood'
##   print isPalindrome('doGood')
##
###Page 51, Figure 4.10
##def fib(x):
##    """Assumes x an int >= 0
##       Returns Fibonacci of x"""
##    global numFibCalls
##    numFibCalls += 1
##    if x == 0 or x == 1:
##        return 1
##    else:
##        return fib(x-1) + fib(x-2)
##
##def testFib(n):
##    for i in range(n+1):
##        global numFibCalls
##        numFibCalls = 0
##        print 'fib of', i, '=', fib(i)
##        print 'fib called', numFibCalls, 'times.'
##
###Page 52, See circle.py
##
###Page 52
##import circle
##print circle.pi
##print circle.area(3)
##print circle.circumference(3)
##print circle.sphereSurface(3)
##
##from circle import *
##print pi
##print circle.pi
##
###Page 53
##nameHandle = open('kids', 'w')
##for i in range(2):
##    name = raw_input('Enter name: ')
##    nameHandle.write(name + '\n')
##nameHandle.close()
##
###Page 54
##nameHandle = open('kids', 'r')
##for line in nameHandle:
##    print line[:-1]
##nameHandle.close()
##
##nameHandle = open('kids', 'w')
##nameHandle.write('Michael\n')
##nameHandle.write('Mark\n')
##nameHandle.close()
##nameHandle = open('kids', 'r')
##for line in nameHandle:
##    print line[:-1]
##nameHandle.close()
##
##nameHandle = open('kids', 'a')
##nameHandle.write('David\n')
##nameHandle.write('Andrea\n')
##nameHandle.close()
##nameHandle = open('kids', 'r')
##for line in nameHandle:
##    print line[:-1]
##nameHandle.close()
