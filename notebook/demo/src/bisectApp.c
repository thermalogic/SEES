
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "ourmath.h"

double fcn(double x)
{
	double  result;
	result = x*x-4;
	return(result);
}

int main()
{
	double  xl, xr, epsilon, root;
	int ier;
    xl=0.1;
    xr=3.2;    ;
    epsilon=0.001;
	// Calculate root  
    bisect(fcn, xl ,xr ,epsilon, &root, &ier);
    // Print answers 
    printf("\n root = %14.7e  ier = %1d", root, ier);
	return 0;
}
