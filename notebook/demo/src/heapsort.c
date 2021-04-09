#include <stdio.h>
#include <stdlib.h>

void max_heapify(int arr[], int n, int i) 
{ 
    int largest = i; // 将最大元素设置为堆顶元素
    int l = 2*i + 1; // left = 2*i + 1 
    int r = 2*i + 2; // right = 2*i + 2 
  
    // 如果 left 比 root 大的话
    if (l < n && arr[l] > arr[largest]) 
        largest = l; 
  
    // I如果 right 比 root 大的话
    if (r < n && arr[r] > arr[largest]) 
        largest = r; 
    
    int temp;
    if (largest != i) 
    { 
        temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp; 
        // 递归地定义子堆
        max_heapify(arr, n, largest); 
    } 
} 

void heapSort(int arr[], int n) 
{ 
    // build Max Heap
    for (int i = n / 2 - 1; i >= 0; i--) 
        max_heapify(arr, n, i); 
  
    int temp;
    // 一个个从堆顶取出元素
    for (int i=n-1; i>=0; i--) 
    { 
        temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp; 
        max_heapify(arr, i, 0); 
    } 
} 

// Print the contents of the given array from iLeft to iRight (inclusive)
void print(const int a[], int iLeft, int iRight) {
   printf("{");
   for (int i = iLeft; i <= iRight; ++i) {
      printf("%d", a[i]);
      if (i < iRight) printf(",");
   }
   printf("}\n");
}


int main() {
   const int SIZE = 9;
   int a[] = {56, 24, 93, 17,77, 31, 44,55,20};
 
   print(a, 0,SIZE-1);
   heapSort(a, SIZE);
   print(a, 0,SIZE-1);
}
