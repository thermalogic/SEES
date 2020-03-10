
#include <stdio.h> 
#include "SumArray.h"
#include "funs.h"

int main() {
    
     int a1[] = {8, 4, 5, 3, 2};
     int len= sizeof(a1)/sizeof(*a1);
     printf("sum is %d\n", sum(a1,  len));  // sum is 22
    
     int n =5;
     printf("the factorial of  %d is %d\n",n,factorial(n));  // 5!=120
     return 0;
}
