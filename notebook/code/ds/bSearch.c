
/* Search an array for a key using Binary Search (BinarySearch.c) */

#include "bSearch.h"

#include <stdio.h>
 
int binarySearch(const int a[], int iLeft, int iRight, int key);
void print(const int a[], int iLeft, int iRight);
  
// Search the array for the given key
// If found, return array index; otherwise, return -1
int bSearch(const int a[], int size, int key) {
   // Call recursive helper function
   return binarySearch(a, 0, size-1, key);
}
 
// Recursive helper function for binarySearch
int binarySearch(const int a[], int iLeft, int iRight, int key) {
  
   // For tracing the algorithm
   print(a, iLeft, iRight);
 
   // Test for empty list
   if (iLeft > iRight) return -1;
 
   // Compare with middle element
   int mid = (iRight + iLeft) / 2;  // truncate
   if (key == a[mid]) {
      return mid;
   } else if (key < a[mid]) {
      // Recursively search the lower half
      binarySearch(a, iLeft, mid - 1, key);
   } else {
      // Recursively search the upper half
      binarySearch(a, mid + 1, iRight, key);
   }
}

// Print the contents of the given array from iLeft to iRight (inclusive)
void print(const int a[], int iLeft, int iRight) {
   printf("{");
   for (int i = iLeft; i <= iRight; ++i) {
      printf("%d",a[i]);
      if (i < iRight) printf(",");
   }
   printf("} \n");
}