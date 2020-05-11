
#include <stdio.h> 
#include "statistics.h"

int main() {
     double a[] = {8, 4, 5, 3, 2};
     int length = sizeof(a)/sizeof(double);  
     printf("mean is %f\n", mean(a,length)); 
     return 0;
}
