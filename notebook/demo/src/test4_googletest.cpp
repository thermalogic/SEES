
#include "region4.h"
#include <gtest/gtest.h>
using ::testing::InitGoogleTest;

//  T,p
double tab35[3][2] = {{300, 0.00353658941},
                      {500, 2.63889776},
                      {600, 12.3443146}};
// p,T
double tab36[3][2] = {{0.1, 372.755919},
                      {1, 453.035632},
                      {10, 584.149488}};

// Test Region4: Saturation line
TEST(Region4Test, SaturationlineTest)
{
  for (int i = 0; i < 3; i++)
  {
    double T = tab35[i][0];
    EXPECT_NEAR(tab35[i][1], pSat(T), 1.0e-6);
  }
  for (int i = 0; i < 3; i++)
  {
    double p = tab36[i][0];
    EXPECT_NEAR(tab36[i][1], TSat(p), 1.0e-6);
  }
}

int main(int argc, char **argv)
{
  InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
