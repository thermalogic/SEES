
/*
   Gauss Elimination Method 
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
                    // make the elements below the pivot elements equal to zero or elimnate the variables
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
        x[i]=b[i];    //1 make the variable to be calculated equal to the rhs of the last equation
        for (j = i + 1; j < nrows; j++)
        {
            x[i] -= a[i][j] * x[j]; //2 then subtract all the lhs values except the coefficient of the variable whose value 
        }
        x[i] /=a[i][i];  // 3 now finally divide the rhs by the coefficient of the variable to be calculated

    }
}
