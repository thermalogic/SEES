/*
  Numerical Recipes http://numerical.recipes
*/ 
#include <math.h>
#include "ourmath.h"

double sign(double a, double b)
{
	if (b < 0.0)
		return (-fabs(a));
	else
		return (fabs(a));
}

void bisect(Fun f, double a, double b, double eps, double *root, int *ier)
{
	/*
	The program uses the bisection method to solve 	the equation
		f(x) = 0.
	The solution is to be in [a,b] and it is assumed 	that
		f(a)*f(b) <= 0.
	The solution is returned in root, and it is to	be in error by at most eps.
	
	ier is an error indicator.
	  If ier=0 on completion of the routine, then the 	solution has been computed satisfactorily.
	  If ier=1, then f(a)*f(b) was greater than 0, contrary to assumption.
*/

	const double zero = 0.0, one = 1.0, two = 2.0;
	double c, fa, fb, fc, sfa, sfb, sfc;

	// Initialize
	fa = (*f)(a);
	fb = (*f)(b);
	sfa = sign(one, fa);
	sfb = sign(one, fb);
	if (sfa * sfb > 0.0)
	{
		// The choice of a and b is in error
		*ier = 1;
		return;
	}

	// Create a new value of c, the midpoint of [a,b]
	while (1)
	{
		c = (a + b) / two;
		if (fabs(b - c) <= eps)
		{
			// c is an acceptable solution of f(x)=0
			*root = c;
			*ier = 0;
			return;
		}
		/* The value of c was not sufficiently accurate. 
			Begin a new iteration  */
		fc = (*f)(c);
		if (fc == zero)
		{
			// c is an acceptable solution of f(x)=0
			*root = c;
			*ier = 0;
			return;
		}
		sfc = sign(one, fc);
		if (sfb * sfc > zero)
		{
			//  The solution is in [a,c]
			b = c;
			sfb = sfc;
		}
		else
		{
			//  The solution is in [c,b]
			a = c;
			sfa = sfc;
		}
	}
}
