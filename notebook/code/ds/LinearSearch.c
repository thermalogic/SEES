
/* Search an array for the given key using Linear Search (LinearSearch.c) */
#include <stdio.h>
#include <stdlib.h> 

int linearSearch(const int a[], int size, int key);

// Search the array for the given key
// If found, return array index [0, size-1]; otherwise, return size
int linearSearch(const int a[], int size, int key) {
   for (int i = 0; i < size; ++i) {
      if (a[i] == key) return i;
   }
   return size;
}
 

int main() {
   const int SIZE = 8;
   int a1[8] = {8, 4, 5, 3, 2, 9, 4, 1};
 
   int keys[3]={8,4,99};
   for(int i=0; i<3; i++) 
       printf("%d's index is: %d \n",keys[i],linearSearch(a1,SIZE, keys[i]));
   
   return 0; 
 }
