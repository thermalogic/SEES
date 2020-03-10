
#include "funs.h"

// x[0]*x[1]*...*x[n-1]
double dprod(const double *x, int length)
{
    double y = 1.0;
    const double *end = x + length; // Points one past the last element.
    
    if(length <= 0 )                 
       return 0.0;
                                             
    for (const double *p = x; p < end; ++p)  // walking a pointer through the array.
       y *=(*p);                                  
   return y;
}

// The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
//  For example,5!=5*4*3*2*1=120
//  The value of 0! is 1 
int factorial(int n)
{
    if (n == 0 ) {
        return 1;
    }
    else 
    {
        return n * factorial(n - 1);
    }
}
