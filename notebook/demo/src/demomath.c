
#include <stdio.h> 
#include "statistics.h"
#include "number.h"

int main() {
    
     double a[] = {8, 4, 5, 3, 2};
     int len= sizeof(a)/sizeof(*a);
     printf("mena is %f\n", mean(a,  len)); 
    
     int n =5;
     printf("the factorial of  %d is %d\n",n,factorial(n));  // 5!=120
     return 0;
}
