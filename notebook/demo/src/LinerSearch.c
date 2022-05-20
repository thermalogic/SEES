/*

 Search an array for the given key using Linear Search (LinearSearch.c)

*/
#include <stdio.h>
#include <stdlib.h>

int linearSearch(const int a[], int size, int key);

// Search the array for the given key
//   1 If found, return array index [0, size-1];
//   2 otherwise, return size: 99's index is: 8
int linearSearch(const int a[], int size, int key)
{
    for (int i = 0; i < size; ++i)
    {
        if (a[i] == key)
            return i;
    }
    return size;
}