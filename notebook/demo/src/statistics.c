
#include "statistics.h"

double  mean(double data[], int size)
{
  /* Compute the arithmetic mean of a dataset using the recurrence relation 
     mean_(n) = mean(n-1) + (data[n] - mean(n-1))/(n+1)   */

  double mean = 0;
  for(int  i = 0; i < size; i++)
  {
      mean += (data[i] - mean) / (i + 1);
   }
  return mean;
}
