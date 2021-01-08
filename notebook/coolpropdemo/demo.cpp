/* 
The example use the shared library of CoolProp in c

The library: libCoolProp.dll or CoolProp_x64.dll

g++  -o ./bin/demo  -DCOOLPROP_LIB demo.cpp -I./include -L./bin -lCoolProp

./bin/demo

*/

#include "CoolPropLib.h"
#include <iostream>
#include <iomanip>

int main()
{
    double value=PropsSI("P","T",273.15+0,"Q",0,"R134a");
    std::cout << std::setiosflags(std::ios::fixed)  << value << std::endl;
    return 1;
}