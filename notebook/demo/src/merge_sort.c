
#include "merge_sort.h"

// Merge two halves in  [iLeft,middle], [middle+1, iRight]
void merge(int a[], int iLeft, int middle, int iRight, int work[])
{
    int size = iRight - iLeft + 1;
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
      merge(a, iLeft,middle, iRight, work);
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
