/* 
The example use a MinGW64 64-bit stdcall dll of CoolProp:

g++  -m64 -O3 -o ./bin/demo.exe  -DCOOLPROP_LIB demo.cpp -I./include -L./lib -lCoolProp
*/

#define EXPORT_CODE extern "C" __declspec(dllimport)
#define CONVENTION __stdcall
#include "CoolPropLib.h"
#undef EXPORT_CODE
#undef CONVENTION

#include <iostream>
//---------------------------------------------------------------------------
int main()
{
    std::cout <<"Demo CoolProp"<< std::endl;
    std::cout << PropsSI("T","P",101325,"Q",0,"Water") << std::endl;
    return 1;
}