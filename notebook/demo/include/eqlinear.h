/*
   Gauss Methods 
*/
#ifndef EQLINEAR_H
#define EQLINEAR_H

// Gauss Elimination Method 
void gauss(int nrows, double **a, double *b, double *x);

//Augmented matrix and Pivoting
void gauss_am_pivoting(int nrows,double **a, double *x);

#endif /* EQLINEAR_H */
