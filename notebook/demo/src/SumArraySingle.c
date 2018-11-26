
#include <stdio.h>  

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

int main() {
     int a1[] = {8, 4, 5, 3, 2};
     printf("sum is %d\n", sum(a1, 5));  // sum is 22
     return 0;
}
