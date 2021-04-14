#include <stdio.h>
#include <stdlib.h>

void max_heapify(int arr[], int n, int i) 
{ 
    int largest = i; 
    int l = 2*i + 1; // left = 2*i + 1 
    int r = 2*i + 2; // right = 2*i + 2 
  
    if (l < n && arr[l] > arr[largest]) 
        largest = l; 
  
    if (r < n && arr[r] > arr[largest]) 
        largest = r; 
    
    int temp;
    if (largest != i) 
    { 
        temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp; 
        max_heapify(arr, n, largest); 
    } 
} 

void heapSort(int arr[], int n) 
{ 
    for (int i = n / 2 - 1; i >= 0; i--) 
        max_heapify(arr, n, i); 
  
    int temp;
    for (int i=n-1; i>=0; i--) 
    { 
        temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp; 
        max_heapify(arr, i, 0); 
    } 
} 

void print(const int a[], int iLeft, int iRight) {
   printf("{");
   for (int i = iLeft; i <= iRight; ++i) {
      printf("%d", a[i]);
      if (i < iRight) printf(",");
   }
   printf("}\n");
}


int main() {
   const int SIZE = 7;
   int a[] = {47,70,86, 46,44,45,66};
 
   print(a, 0,SIZE-1);
   heapSort(a, SIZE);
   print(a, 0,SIZE-1);
}
