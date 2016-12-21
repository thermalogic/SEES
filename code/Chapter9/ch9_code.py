##def f(i):
#Page 113
   """Assumes i is an int and i >= 0"""
   answer = 1
   while i >= 1:
      answer *= i
      i -= 1
   return answer

#Page 114
def linearSearch(L, x):
   for e in L:
      if e == x:
         return True
   return False

#Page 115
def fact(n):
   """Assumes n is a natural number
      Returns n!"""
   answer = 1
   while n > 1:
      answer *=  n
      n -= 1
   return answer

#Page 115, Figure 9.1
def squareRootExhaustive(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   step = epsilon**2
   ans = 0.0
   while abs(ans**2 - x) >= epsilon and ans*ans <= x:
       ans += step
   if ans*ans > x:
      raise ValueError
   return ans

#Page 116, Figure 9.3
def squareRootBi(x, epsilon):
   """Assumes x and epsilon are positive floats & epsilon < 1
      Returns a y such that y*y is within epsilon of x"""
   low = 0.0
   high = max(1.0, x)
   ans = (high + low)/2.0
   while abs(ans**2 - x) >= epsilon:
      if ans**2 < x:
         low = ans
      else:
         high = ans
      ans = (high + low)/2.0
   return ans

#Page 116
def f(x):
   """Assume x is an int > 0"""
   ans = 0

   #Loop that takes constant time
   for i in range(1000):
      ans += 1
   print('Number of additions so far', ans)

   #Loop that takes time x
   for i in range(x):
      ans += 1
   print('Number of additions so far', ans)

   #Nested loops take time x**2
   for i in range(x):
      for j in range(x):
         ans += 1
         ans += 1
   print('Number of additions so far', ans)
   return ans

#Page 119
def intToStr(i):
   """Assumes i is a nonnegative int
      Returns a decimal string representation of i"""
   digits = '0123456789'
   if i == 0:
      return '0'
   result = ''
   while i > 0:
      result = digits[i%10] + result
      i = i//10
   return result

def addDigits(n):
   """Assumes n is a nonnegative int
      Returns the sum of the digits in n"""
   stringRep = intToStr(n)
   val = 0
   for c in stringRep:
      val += int(c)
   return val

def addDigits(s):
   """Assumes s is a str each character of which is a
         decimal digit.
      Returns an int that is the sum of the digits in s"""
   val = 0
   for c in s:
      val += int(c)
   return val

#Page 120
def factorial(x):
   """Assumes that x is a positive int
      Returns x!"""
   if x == 1:
      return 1
   else:
      return x*factorial(x-1)

#Page 121, Figure 9.3
def isSubset(L1, L2):
   """Assumes L1 and L2 are lists.
      Returns True if each element in L1 is also in L2
      and False otherwise."""
   for e1 in L1:
      matched = False
      for e2 in L2:
         if e1 == e2:
            matched = True
            break
      if not matched:
         return False
   return True

#Page 121, Figure 9.4
def intersect(L1, L2):
   """Assumes: L1 and L2 are lists
      Returns a list that is the intersection of L1 and L2"""
   #Build a list containing common elements
   tmp = []
   for e1 in L1:
      for e2 in L2:
         if e1 == e2:
            tmp.append(e1)
   #Build a list without duplicates
   result = []
   for e in tmp:
      if e not in result:
         result.append(e)
   return result

#Page 121, Figure 9.5
def getBinaryRep(n, numDigits):
   """Assumes n and numDigits are non-negative ints
      Returns a numDigits str that is a binary
      representation of n"""
   result = ''
   while n > 0:
      result = str(n%2) + result
      n = n//2
   if len(result) > numDigits:
      raise ValueError('not enough digits')
   for i in range(numDigits - len(result)):
      result = '0' + result
   return result

def genPowerset(L):
   """Assumes L is a list
      Returns a list of lists that contains all possible
      combinations of the elements of L.  E.g., if
      L is [1, 2] it will return a list with elements
      [], [1], [2], and [1,2]."""
   powerset = []
   for i in range(0, 2**len(L)):
      binStr = getBinaryRep(i, len(L))
      subset = []
      for j in range(len(L)):
         if binStr[j] == '1':
            subset.append(L[j])
      powerset.append(subset)
   return powerset
