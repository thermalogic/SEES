
/*
 Sorting an array using Selection Sort (SelectionSort.c) 
*/

#include <stdio.h>
#include <stdlib.h>

void selectionSort(int a[], int size);
void print(const int a[], int iMin, int iMax);

// Sort the given array of size using selection sort
void selectionSort(int a[], int size)
{
   int temp; // for swaping
   for (int i = 0; i < size - 1; ++i)
   {
      // for tracing
      print(a, 0, i - 1);
      print(a, i, size - 1);

      // [0, i-1] already sort
      // Search for the smallest element in  remaining unsorted array [i, size-1] and swap with a[i]
      int min_idx = i; // assume fist element is the smallest
      for (int j = i + 1; j < size; ++j)
      {
         if (a[j] < a[min_idx])
            min_idx = j;
      }
      // # Swap the found minimum element with  the first element  a[minIndex]   
      if (min_idx != i)
      { 
         temp = a[i];
         a[i] = a[min_idx];
         a[min_idx] = temp;
      }

      // for tracing
      printf("=> ");
      print(a, 0, i - 1);
      print(a, i, size - 1);
      printf("\n");
   }
}

// Print the contents of the array in [iMin, iMax]
void print(const int a[], int iMin, int iMax)
{
   printf("{");
   for (int i = iMin; i <= iMax; ++i)
   {
      printf("%d", a[i]);
      if (i < iMax)
         printf(",");
   }
   printf("}");
}

int main()
{
   const int SIZE = 7;
   int a[7] = {7, 4, 5, 9, 8, 2, 1};
   print(a, 0, SIZE - 1);
   printf("\n");
   selectionSort(a, SIZE);
   print(a, 0, SIZE - 1);
   printf("\n");

   return 0;
}
