
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "roots.h"

double fcn(double x)
{
	double result;
	result = x * x - 4;
	return result;
}

int main()
{
	double xl, xu, epsilon, root;
	int ier;
	xl = 0.1;
	xu = 3.2;
	epsilon = 0.001;
	// Calculate root
	ier=rtbis(fcn, xl, xu, epsilon, &root);
	// Print answers
	printf("root = %14.7e  ier = %1d", root, ier);
	return 0;
}
