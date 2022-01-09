
#include <stdio.h>
#include <stdlib.h>
  
// A comparator function used by qsort
int compare(const void * a, const void * b)
{
    return ( *(int*)a - *(int*)b );
}

void printArr(int arr[], int n)
{
    int i;
    for (i = 0; i < n; ++i)
        printf("%d ", arr[i]);
}
 
// Driver program to test above function
int main()
{
    int arr[] = {1, 6, 5, 2, 3, 9, 4, 7, 8};
  
    int size = sizeof(arr) / sizeof(arr[0]);
    qsort((void*)arr, size, sizeof(arr[0]), compare);
  
    printf("Output array is\n");
    printArr(arr, size);
  
    return 0;
}
