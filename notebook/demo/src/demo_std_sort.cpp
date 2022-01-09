
#include <iostream>     // std::cout
#include <algorithm>    // std::sort

using namespace std;

bool myfunction (int i,int j) { return (i>j); }

int main () {
  int a[8] = {32,71,12,45,26,80,53,33};
  int b[8] = {32,71,12,45,26,80,53,33};
  // using default comparison (operator <):
  sort (a,a+8); 
  for (int i=0;i<8; i++)
      cout << a[i]<<" ";
  cout << '\n';

  // using my comparison:
  sort (b,b+8, myfunction);
  for (int i=0;i<8; i++)
     cout << b[i]<<" ";
  cout << '\n';
  return 0;
}
