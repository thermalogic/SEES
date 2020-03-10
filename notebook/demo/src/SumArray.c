
#include "SumArray.h"

/*
   Return the sum of the given array
*/

int sum(const int array[], int length)
{
    int sum = 0;
    if ( length <= 0 )                 
        return 0;
    
    for (int i = 0; i < length; ++i) {
        sum += array[i];
    }
    return sum;
}
