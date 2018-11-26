
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
