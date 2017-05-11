
#include <stdio.h>
#include "funs.h"

void hello()
{
   printf("C says Hello world!\n");
}

double dprod(double *x, int n)
{
    double y = 1.0;
    for (int i = 0; i < n; i++)
    {
        y *= x[i];
    }
    return y;
}

//The linear time algorithm for finding Fibonacci numbers
unsigned long LinearFibonacci(int n)
{
  unsigned long fib;
  if (n< 0)
      return -1;
  
  // base case 0 or 1
  if (n == 0||n==1)
      return 1;
 
  unsigned long f1=1,f2 = 1;
  for(int i=2; i<=n; i++)
  {
    fib = f1 + f2;
    f2=f1;
    f1=fib;
  }    
  return fib;
}