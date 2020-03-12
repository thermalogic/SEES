#ifndef ROOTS_H
#define ROOTS_H

#include <math.h>
// function definition
typedef double (*fun)(double);

int rtbis(fun func,double , double, double ,double *);

#endif
