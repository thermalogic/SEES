
#include <stdio.h>
#include <stdlib.h> 
#include "bSearch.h" 

int main() {
   const int SIZE = 10;
   int a1[10] = {1, 4, 5, 8, 12, 19, 24, 31, 43, 55}; // sorted
 
   int keys[4]={8,12,24,21};
   for(int i=0; i<4; i++) 
       printf("%d's index is: %d \n",keys[i],bSearch(a1,  SIZE, keys[i]));
   
   return 0; 
}