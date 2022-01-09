
/* Sorting an array using Merge Sort (MergeSort.c) */
#include <stdio.h>
#include <stdlib.h>

void print(const int a[], int iLeft, int iRight);

void merge(int a[], int iLeft, int iRight, int work[]);
void merge_sort_range(int a[], int iLeft, int iRight, int work[]);

void merge_sort(int a[], int size);

// Merge two halves in  [iLeft,middle], [middle+1, iRight]
void merge(int a[], int iLeft, int iRight, int work[])
{
   int size = iRight - iLeft + 1;
   int middle=(iRight+iLeft)/2;
 
   // 1 comparing the values of elements
    //  Look at the first element of each list, and move the smaller of the two to the end of the result list.
    int iL = iLeft;
    int iR = middle+1;
    int iResult = 0;
    while (iL <= middle && iR <= iRight)
    {
         if (a[iL] <= a[iR])
         {
             work[iResult++] = a[iL++];
          }
          else
          {
             work[iResult++] = a[iR++];
          }
   }
  
  // 2 Copy the remaining left or right into work
   while (iL <= middle)
         work[iResult++] = a[iL++];
   while (iR <= iRight)
         work[iResult++] = a[iR++];
 
   // for tracing
   print(a, iLeft, middle);
   print(a, middle+1, iRight);
   printf("=> ");
   print(work, 0, size - 1);
   printf("\n");
 
   // 3 Copy the work back to the original array
   for (iResult = 0, iL = iLeft; iResult < size; ++iResult, ++iL)
   {
      a[iL] = work[iResult];
   }
}

// Sort the given array in [iLeft, iRight]
void merge_sort_range(int a[], int iLeft, int iRight, int work[])
{
   if ((iRight - iLeft) >= 1) { 
      // more than 1 elements, divide and sort
      // Divide into left and right half
      int middle = (iRight + iLeft) / 2;   // truncate
     
      // Recursively sort each half
      merge_sort_range(a, iLeft, middle, work);
      merge_sort_range(a, middle+1, iRight, work);
 
      // Merge two halves
      merge(a, iLeft, iRight, work);
   }
}
 
// Sort the given array of size
void merge_sort(int a[], int size)
{
   int *work;
   work = (int *)malloc(sizeof(int) * size);
   merge_sort_range(a, 0, size - 1, work);
   free(work); 
}
 
// Print the contents of the given array from iLeft to iRight (inclusive)
void print(const int a[], int iLeft, int iRight)
{
   printf("{");
   for (int i = iLeft; i <= iRight; ++i) {
      printf("%d", a[i]);
      if (i < iRight) printf(",");
   }
   printf("} ");
}

 
int main() {
   const int SIZE = 4;
   int a[4] = {6, 2, 9,3};
 
   print(a, 0, SIZE - 1);
   printf("\n");
   merge_sort(a, SIZE);
   print(a, 0, SIZE - 1);
   printf("\n");
   return 0;
}
