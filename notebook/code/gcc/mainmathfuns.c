
#include <stdio.h>
#include "mathfuns.h"
 
int main() {
    double a=5.3;
    double b=6.1;
    double radd=fadd(a,b);
    double rmul=fmul(a,b);
    printf("%.3f + %.3f = %.3f \n",a,b,radd);
    printf("%.3f * %.3f = %.3f \n",a,b,rmul);
    return 0;
}