#include <string>
#include <iostream>
#include <tuple>

using namespace std;

int main()
{
  tuple<int,float,long> tup{1,2.0,3};
  cout << get<0>(tup)<<" "<<get<1>(tup)<<endl;
  // C++17, decompose a tuple into individual vars
  auto [a, b, c] = tup;
  std::cout << a << ", " << b << ", " << c << "\n";
  return 0;
}
