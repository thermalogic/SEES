#include"MaxHeap.h"
 
int main() {
	int arr[] = { 7, 8, 2, 3, 4, 5, 1, 6, 9 };
	MaxHeap<int> maxheap(arr, 9);
 
	maxheap.insert(13);
	maxheap.display();
	int temp;
	maxheap.removeMax(temp);
	cout << "delete the top item of heap: " << temp << endl;
	cout << "after the delete, display: " << endl;
	maxheap.display();
	return 0;
}
