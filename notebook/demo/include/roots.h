#ifndef ROOTS_H
#define ROOTS_H

#include <math.h>
// function definition
typedef double (*fun)(double);

int rtbis(fun func,double x1, double x2, double xacc,double *rtb);
/*
	The program uses the bisection method to solve the equation
		f(x) = 0.
	The solution is to be in [x1,x2] and it is assumed that
		f(x1)*f(x2) <= 0.
	The solution is returned in rtb, and it is to be in error by at most xacc.
	
	return value is an error indicator.
	  If =0, the solution has been computed satisfactorily.
	  If =1, f(x1)*f(x2) was greater than 0, contrary to assumption 
      If =2, exceeded the maximum number of iteration 
*/
#endif
