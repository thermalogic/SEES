
#include <stdio.h>
#include "funs.h"
 
int main() {
    hello();
    double x[5]={1.0,2.0,3.0,4.0,5.0};
    int n=5;
    double r=dprod(x,n);
    printf("dprod %.2f ",r);
    return 0;
}