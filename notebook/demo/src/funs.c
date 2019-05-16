
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
