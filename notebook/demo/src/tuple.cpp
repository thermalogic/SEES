/*

cl /std:c++17 tuple.cpp

*/
#include <string>
#include <iostream>
#include <tuple>

using namespace std;

int main()
{
  tuple<int,string,float> tup{1,"str2",3.21};
  cout << get<0>(tup)<<" "<<get<1>(tup)<<endl;
  // C++17, decompose a tuple into individual vars
  auto [a, b, c] = tup;
  cout << a << ", " << b << ", " << c << "\n";
  return 0;
}
