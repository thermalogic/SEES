
/*
  Augmented matrix and Pivoting
    nrows  - Matrix dimensions
    a - Matrix a[nrows][nrows+1]
	a[row][nrows] - Right hand side vector b[nrows]
	x  - Desired solution vector
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "eqlinear.h"
void gauss_am_pivoting(int nrows,double **a, double *x)
{
    int i,j,k;
    double c;
           
    for (i = 0; i < nrows; i++) 
        for (k = i + 1; k < nrows; k++)
            if ((double)fabs(a[i][i]) < (double)fabs(a[k][i]))
                for (j = 0; j <=nrows; j++)
                {
                    double temp = a[i][j];
                    a[i][j] = a[k][j];
                    a[k][j] = temp;
                }
 
    // loop to perform the gauss elimination
    for (i = 0; i <nrows - 1; i++)
        for (k = i + 1; k <nrows; k++)
        {
             c = a[k][i] / a[i][i];
            for (j = 0; j <= nrows; j++)
                a[k][j] = a[k][j] - c * a[i][j]; 
        }
    
    // back-substitution
    for (i = nrows - 1; i >= 0; i--)
    {                            
        x[i] =a[i][nrows];        
        for (j = 0; j < nrows; j++)
            if (j != i)                              
                x[i] = x[i] - a[i][j] * x[j];
        x[i] = x[i] / a[i][i]; 
    }
}
