
#include "region4.h"
#include "unity.h"

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

void setUp(void) {}

void tearDown(void) {}


void test_SaturationP(void)
{
  //  Saturation P line
  for (int i = 0; i < 3; i++)
  {
    double T = tab35[i][0];
    TEST_ASSERT_EQUAL_FLOAT(tab35[i][1], pSat(T));
  }
}

void test_SaturationT(void)
{
  //  Saturation T line
  for (int i = 0; i < 3; i++)
  {
    double p = tab36[i][0];
    TEST_ASSERT_EQUAL_FLOAT(tab36[i][1], TSat(p));
  }
}
 
int main(void)
{
  UNITY_BEGIN();
  RUN_TEST(test_SaturationP);
  RUN_TEST(test_SaturationT);
  return UNITY_END();
}
