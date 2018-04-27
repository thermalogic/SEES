
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
