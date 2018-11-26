
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
