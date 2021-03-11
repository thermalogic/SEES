
/* 
The example use the shared library of CoolProp in c

The library: libCoolProp.dll or CoolProp_x64.dll

g++ -DCOOLPROP_LIB -o ./bin/main   main.c -I./include -L./bin -lCoolProp
       
./bin/main

*/

#include "CoolPropLib.h"
#include <stdio.h>

int main() {
     double value=PropsSI("P","T",273.15+0,"Q",0,"R134a");
     printf("%f\n", value); 
     return 0;
}