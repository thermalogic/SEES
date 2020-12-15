
#include <stdio.h> 
#include "R134aSat.h"

int main() {
     double t=-20;
     printf("Temp: %f, Saturation P(MPa) is %f\n",t, pSat(t));  
     return 0;
}
