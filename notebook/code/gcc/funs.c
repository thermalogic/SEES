
#include "funs.h"
#include <stdio.h>

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