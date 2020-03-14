/*
   Gauss Method 
    nrows  - Matrix dimensions
    a - Matrix a[nrows][nrows]
	b - Right hand side vector b[nrows]
	x  - Desired solution vector
*/
#ifndef EQLINEAR_H
#define EQLINEAR_H

// Gauss Elimination Method 
void gauss(int nrows, double **a, double *b, double *x);

// Gauss Elimination Method + Row Pivoting

void gauss_pivoting(int nrows,double **a, double *b, double *x);

#endif /* EQLINEAR_H */
