
#include "cregion4.h"
#include <iostream>
using namespace std;

//  T,p
static const double tab35[3][2] = {
    {300, 0.00353658941},
    {500, 2.63889776},
    {600, 12.3443146}};

// p,T
static const double tab36[3][2] = {
    {0.1, 372.755919},
    {1, 453.035632},
    {10, 584.149488}};

void testSaturationline(void)
{
  //  Saturation line

  for (int i = 0; i < 3; i++)
  {
    double T = tab35[i][0];
    cout<<"("<<T<<","<<pSat(T)<<")"<<endl;
  }

  for (int i = 0; i < 3; i++)
  {
    double p = tab36[i][0];
    TSat(p);
    cout<<"("<<p<<","<<TSat(p)<<")"<<endl;
  }
}

int main(void)
{
  testSaturationline();
}
