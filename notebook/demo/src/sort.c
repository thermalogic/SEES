
#include "sort.h"
// Sort the given array of size
void bubbleSort(int a[], int size)
{
   bool done = false; // terminate if no more swap thru a pass
   int temp;     // use for swapping

   while (!done)
   {
      done = true;
      // Pass thru the list, compare adjacent items and swap
      // them if they are in wrong order
      for (int i = 0; i < size - 1; ++i)
      {
         if (a[i] > a[i + 1])
         {
            temp = a[i];
            a[i] = a[i + 1];
            a[i + 1] = temp;
            done = false; // swap detected, one more pass
         }
      }
   }
}

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

