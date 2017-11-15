
/* linear searching an array using The GNU C Library ：lsearch (gnulsearch.c) */

#include <stdio.h>
#include <stdlib.h> 
#include <search.h> 

int compare_ints (const void *a, const void *b)
{
   return (*(int*)a - *(int*)b);  
}

int main() {
   unsigned int SIZE = 8;
   int values[8] = {8, 4, 5, 3, 2, 9, 4, 1};
   int keys[3]={8,4,99};
   int *pItem; 
   int i;
   for(i=0; i<3; i++) 
   { 
      pItem = (int*)lfind(&keys[i],&values[0],&SIZE,sizeof(int),compare_ints);
      if (pItem!=NULL)
         printf("%d is in the array \n",*pItem);
      else  
        printf ("%d is not in the array \n",keys[i]);  
   }
   int rawSIZE=SIZE; 
   for(i=0; i<3; i++) 
   { 
      pItem = (int*)lsearch(&keys[i],&values[0],&SIZE,sizeof(int),compare_ints);
      if (SIZE>rawSIZE)
      {
         printf("%d is added into the array \n",*pItem);
         rawSIZE=SIZE;
      }    
      else 
        printf("%d is in the array \n",*pItem);
   }
   return 0;
}
    