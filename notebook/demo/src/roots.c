/*
  Numerical Recipes http://numerical.recipes
*/ 
#include <math.h>
#include "roots.h"

int rtbis(fun func,double y,double x1, double x2, double xacc,double *rtb)
{
 /*
	The program uses the bisection method to solve the equation
		f(x)-y = 0.
	The solution is to be in [x1,x2] and it is assumed that
		(f(x1)-y)*(f(x2)-y) <= 0.
	The solution is returned in rtb, and it is to be in error by at most xacc.
	
	return value is an error indicator.
	  If =0, the solution has been computed satisfactorily.
	  If =1, (f(x1)-y)*(f(x2)-y) was greater than 0, contrary to assumption 
      If =2, exceeded the maximum number of iteration 
*/
	const int IMAX=100; // the maximum number of iteration
    float dx,f,fmid,xmid;

	f=(*func)(x1)-y;
	fmid=(*func)(x2)-y;
	if (f*fmid >= 0.0) // endpoints do not straddle y=0
       return 1; 
    // init the root value: rtb
	*rtb = f < 0.0 ? (dx=x2-x1,x1) : (dx=x1-x2,x2);
	for (int i=1;i<=IMAX;i++) {
		fmid=(*func)(xmid=(*rtb)+(dx *= 0.5))-y;
		if (fmid <= 0.0) *rtb=xmid;
		if (fabs(dx) < xacc || fmid == 0.0) 
           return 0;
  	}
    // Exceeded the maximum number of iteration
    return 2;
}
