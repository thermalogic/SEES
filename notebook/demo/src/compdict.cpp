/*
g++ -std=c++11 -o demo  compdict.cpp
*/

#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

typedef string (*myFunc)(void);
typedef unordered_map<string, myFunc> compdict;

/* The functions */

string Boiler(void)
{
    return  "- BOILER -";
}

string Condenser(void)
{
    return  "-CONDENSER-";
}

string TurbineEx1(void)
{
     return  " -TURBINE-EX1- "; 
}

int main()
{
    compdict comps = {{"BOILER", &Boiler}, { "CONDENSER",  &Condenser},{"TURBINE-EX1", &TurbineEx1}};
    
    cout <<comps["BOILER"]()<< endl;
    
    unordered_map<string, myFunc>::iterator iter;
    for (iter = comps.begin(); iter != comps.end(); iter++)
    {
        cout << "key = " << iter->first << "  result of the function "<< iter->second() << endl;
    }
    return 0;
}
