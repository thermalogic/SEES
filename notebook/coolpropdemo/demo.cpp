/* 
The example use the shared library of CoolProp in c++

g++ -DCOOLPROP_LIB -o ./bin/demo  demo.cpp -I./include -L./bin -lCoolProp

./bin/demo

*/

#include <iostream>
#include <iomanip>
#include "CoolPropLib.h"

int main()
{
    double value=PropsSI("P","T",273.15+0,"Q",0,"R134a");
    std::cout << std::setiosflags(std::ios::fixed)  << value << std::endl;
    return 1;
}
