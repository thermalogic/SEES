
/* 
The example use the static library of CoolProp in c

The library: ./lib/libCoolProp.a

g++ -o ./bin/mainstatic   main.c -I./include -L./lib -lCoolProp
       
./bin/mainstatic

*/

#include "CoolPropLib.h"
#include <stdio.h>

int main() {
     double value=PropsSI("P","T",273.15+0,"Q",0,"R134a");
     printf("%f\n", value); 
     return 0;
}
