
/*
   Gauss Pivoting  Elimination Method 
    nrows  - Matrix dimensions
    a - Matrix a[nrows][nrows]
	b - Right hand side vector b[nrows]
	x  - Desired solution vector
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "eqlinear.h"

void gauss_pivoting(int nrows, double **a, double *b, double *x)
{
    int i, j, k, m, rowx;
    double xfac, temp, temp1, amax;

    /*  Do the forward reduction step. */
    rowx = 0;                   /* Keep count of the row interchanges */
    for (k = 0; k < nrows; ++k) //
    {
        amax = (double)fabs(a[k][k]);
        m = k;                          // pivoting row
        for (i = k + 1; i < nrows; i++) // the next row k
        {                               /* Find the row with largest pivot */
            xfac = (double)fabs(a[i][k]);
            if (xfac > amax)
            {
                amax = xfac;
                m = i;
            }
        }
        /* Row interchanges: row m->k */
        if (m != k)
        {
            rowx = rowx + 1;
            temp1 = b[k];
            b[k] = b[m];
            b[m] = temp1;
            for (j = k; j < nrows; j++)
            {
                temp = a[k][j];
                a[k][j] = a[m][j];
                a[m][j] = temp;
            }
        }
        // reduction
        for (i = k + 1; i < nrows; ++i)
        {
            xfac = a[i][k] / a[k][k];
            for (j = k + 1; j < nrows; ++j)
            {
                a[i][j] = a[i][j] - xfac * a[k][j];
            }
            b[i] = b[i] - xfac * b[k];
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
