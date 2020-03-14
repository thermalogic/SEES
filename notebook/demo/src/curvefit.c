/*
   x[size], y[size]
   n is the degree of Polynomial 
   a[n+1] is the polynomial regression coefficients (
*/

#include <math.h>
#include<stdlib.h> 
#include "curvefit.h"
#include "eqlinear.h"

void c_polyfit(double x[], double y[], int size, int n, double a[])
{
    int i, j;
    double X[2 * n + 1]; //Array that will store the values of sigma(xi),sigma(xi^2),....sigma(xi^2n)
    double **B;
    B=(double**)malloc(sizeof(double)*(n+1)); 
    for(i=0;i<(n+1);i++)  
        B[i]=(double*)malloc(sizeof(double)*(n+2));
    double Y[n+1];  // Array to store the values of sigma(yi),sigma(xi*yi),sigma(xi^2*yi)...sigma(xi^n*yi)
  
    for (i = 0; i < 2 * n + 1; i++)
    {
        X[i] = 0;
        for (j = 0; j < size; j++)
            X[i] = X[i] + pow(x[j], i); //consecutive positions of the array will store N,sigma(xi),sigma(xi^2),....sigma(xi^2n)
    }
   
     
    for (i = 0; i <= n; i++)
        for (j = 0; j <= n; j++)
            B[i][j] = X[i + j]; // Build the Normal matrix by storing the corresponding coefficients at the right positions except the last column of the matrix
     
    for (i = 0; i < n+1; i++)
    {
        Y[i] = 0;
        for (j = 0; j < size; j++)
           Y[i] = Y[i] + pow(x[j], i) * y[j]; //consecutive positions will store sigma(yi),sigma(xi*yi),sigma(xi^2*yi)...sigma(xi^n*yi)
   }
   for (i = 0; i <= n; i++)
        B[i][n + 1] = Y[i]; // load the values of Y as the last column of B(Normal Matrix but augmented)
   
 
   gauss_am_pivoting(n+1,B,a);
    
   for(i=0;i<(n+1);i++)  
       free(B[i]);
   free(B); 
    
}
