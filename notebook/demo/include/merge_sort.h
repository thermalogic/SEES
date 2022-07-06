
#ifndef MERGE_SORT_H
#define MERGE_SORT_H

#include <stdlib.h>

#ifdef __cplusplus
extern "C"
{
#endif

void merge(int a[], int iLeft, int middle, int iRight, int work[]);
void merge_sort_range(int a[], int iLeft, int iRight, int work[]);    
void merge_sort(int a[], int size);

#ifdef __cplusplus

}
#endif

#endif

