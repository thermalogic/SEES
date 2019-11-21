#include <string>
#include <iostream>
#include <tuple>

using namespace std;

int main()
{
  auto triple = make_tuple(100, 200);
  int x,y;
  cout << get<0>(triple)<<" "<<get<1>(triple)<<endl;
  // Python lets you unpack a tuple into separate variables:
  // x, y = triple
  tie(x, y) = triple;
  cout <<x<<" "<<y<<endl;
  return 0;
}
