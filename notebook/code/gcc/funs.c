
#include <stdio.h>
#include "funs.h"

// x[0]*x[1]*...*x[n-1]
double dprod(double *x, int n)
{
    double y = 1.0;
    for (int i = 0; i < n; i++)
    {
        y *= x[i];
    }
    return y;
}

// The linear time algorithm for finding Fibonacci numbers
//   females(0) =1
//   females(1) = 1
//   females(n + 2) = females(n+1) + females(n）
// n------------                                             
//   f1=  females(n）
//   f2=  females(n+1)
//   fib = f1 + f2;
//   
//    f2=f1; ->females(n+1)
//    f1=fib; ->females(n + 2) 
//n+1----------
//    f1=  females(n+1）
//    f2=  females(n+1+1)
//    fib = f1 + f2;              
//                  
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
    // 1 only add
    fib = f1 + f2; 
    // 2 swap  
    f2=f1; 
    f1=fib;
  }    
  return fib;
}