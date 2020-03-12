
#include "SumArray.h"

/* Function definition
   Return the sum of the given array
*/

int sum(int array[], int size)
{
    int sum = 0;
    int i;
    for (i = 0; i < size; ++i) {
        sum += array[i];
    }
    return sum;
}

double  mean(double data[], int size)
{
  /* Compute the arithmetic mean of a dataset using the recurrence relation 
     mean_(n) = mean(n-1) + (data[n] - mean(n-1))/(n+1)   */

  long double mean = 0;
  for(int  i = 0; i < size; i++)
  {
      mean += (data[i * stride] - mean) / (i + 1);
   }
  return mean;
}
