
/* Sorting an array using The GNU C Library ：Sort (gccqsort.c) */

#include <stdio.h>
#include <stdlib.h> 

int compare_ints (const void * a, const void * b)  
{  
  return ( *(int*)a - *(int*)b );  
}  

int main() {
   const int SIZE = 8;
   int a[8] = {8, 4, 5, 3, 2, 9, 4, 1};
   qsort(a, SIZE, sizeof(int),compare_ints);
   
   for(int i = 0; i <SIZE; i++) 
      printf("%d ", a[i]);
   
  return 0;
}
    