
#include <stdio.h> 
#include "SumArray.h"

int main() {
    
     int a1[] = {8, 4, 5, 3, 2};
     int len= sizeof(a1)/sizeof(*a1);
     printf("sum is %d\n", sum(a1, len));  // sum is 22
     return 0;
}
