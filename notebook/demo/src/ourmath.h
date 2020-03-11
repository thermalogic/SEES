#include <math.h>
// function definition
typedef double (__stdcall *Fun)(double x);

double sign(double, double);
void bisect(Fun f,double, double, double, double *, int *);
