
/* Sorting an array using The GNU C Library ：Sort (gccSort.c) */

#include <stdio.h>
#include <stdlib.h> 


int main() {
   const int SIZE = 8;
   int a[8] = {8, 4, 5, 3, 2, 9, 4, 1};
   qsort(a, SIZE, sizeof(int));
   
   return 0;
}

    