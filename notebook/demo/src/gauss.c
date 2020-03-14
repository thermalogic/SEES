
/*
   Gauss  Elimination Method 
    nrows  - Matrix dimensions
    a - Matrix a[nrows][nrows]
	b - Right hand side vector b[nrows]
	x  - Desired solution vector
	
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "eqlinear.h"

void gauss(int nrows, double **a, double *b, double *x)
{
    int i, j, k;
    double c;

    for (j = 0; j < nrows; j++) /* loop for the generation of upper triangular matrix*/
    {
        for (i = 0; i < nrows; i++)
        {
            if (i > j)
            {
                c = a[i][j] / a[j][j];
                for (k = 0; k < nrows; k++)
                {
                    a[i][k] -= c * a[j][k];
                }
                b[i] -=c*b[j]; 
            }
        }
    }

    /* this loop is for backward substitution*/
    x[nrows-1]=b[nrows-1]/a[nrows-1][nrows-1];
    for (i = nrows - 2; i >= 0; i--)
    {
        x[i]=b[i];
        for (j = i + 1; j < nrows; j++)
        {
            x[i] -= a[i][j] * x[j];
        }
        x[i] /=a[i][i];

    }
}
