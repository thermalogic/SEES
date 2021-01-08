
/* 
The example use the shared library of CoolProp in c

g++ -o ./bin/mainso  -DCOOLPROP_LIB mainso.c -I./include -L./bin -lCoolProp -Wl,-rpath=./bin/ 
     
./bin/mainso

*/

#include "CoolPropLib.h"
#include <stdio.h>

int main() {
     double value=PropsSI("P","T",273.15+0,"Q",0,"R134a");
     printf("%f\n", value); 
     return 0;
}
