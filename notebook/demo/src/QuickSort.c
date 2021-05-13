/* 
 Sorting an array using Quick Sort (QuickSort.c) 

*/
#include <stdio.h>
#include <stdlib.h>
 
void quickSort(int a[], int size);
void quick_Sort(int a[], int left, int right);
void choosePivot(int a[], int left, int right);
int partition(int a[], int left, int right);
void print(const int a[], int left, int right);
 
// Sort the given array of size
void quickSort(int a[], int size) {
   quick_Sort(a, 0, size - 1);
}
 
// Sort the given array in [left, right]
void quick_Sort(int a[], int left, int right) {
   if ((right - left) >= 1) {   // more than 1 elements, need to sort
      choosePivot(a, left, right);
      int pivotIndex = partition(a, left, right);
      quick_Sort(a, left, pivotIndex -  1);
      quick_Sort(a, pivotIndex + 1, right);
   }
}
 
// Choose a pivot element and swap with the right
void choosePivot(int a[], int left, int right) {
   int pivotIndex = (right + left) / 2;
   int temp;
   temp = a[pivotIndex];
   a[pivotIndex] = a[right];
   a[right] = temp;
}
 
// Partition the array [left, right] with pivot initially on the right.
// Return the index of the pivot after partition, all elements to the
// left of pivot are smaller; while to the right are larger.
int partition(int a[], int left, int right) {
   int pivot = a[right];
   int temp;  // for swapping
   int storeIndex = left;
      // Start the storeIndex from left, swap elements smaller than
      //  pivot into storeIndex and increase the storeIndex.
      // At the end of the pass, all elements up to storeIndex are
      //  smaller than pivot.
   for (int i = left; i < right; ++i) {  // exclude pivot
      if (a[i] < pivot) {
         // for tracing
         print(a, left, right);
 
         if (i != storeIndex) {
            temp = a[i];
            a[i] = a[storeIndex];
            a[storeIndex] = temp;
         }
         ++storeIndex;
 
         // for tracing
         printf("=> ");
         print(a, left, right);
         printf("\n");
      }
   }
   // Swap pivot and storeIndex
   a[right] = a[storeIndex];
   a[storeIndex] = pivot;
 
   // for tracing
   print(a, left, storeIndex - 1);
   printf("{ %d }",a[storeIndex]);
   print(a, storeIndex + 1, right);
   printf("\n");
  
   return storeIndex;
}
 
// Print the contents of the given array from left to right (inclusive)
void print(const int a[], int left, int right) {
     printf("{");
   for (int i = left; i <= right; ++i) {
        printf("%d",a[i]);
      if (i < right)   printf(",");
   }
     printf("}");
}

int main() {
   const int SIZE = 8;
   int a[8] = {49,38,65, 97,76, 13, 27,49};
 
   print(a, 0, SIZE - 1);
   printf("\n");
   printf("Sorting ...\n");
   quickSort(a, SIZE);
   print(a, 0, SIZE - 1);
   printf("\n");
  
}  
 
