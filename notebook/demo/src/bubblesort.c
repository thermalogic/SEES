/* Sorting an array using Bubble Sort (BubbleSort.c) */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void bubbleSort(int a[], int size);
void print(const int a[], int size);

// Sort the given array of size
void bubbleSort(int a[], int size)
{
    bool done = false; // terminate if no more swap thru a pass
    int temp;          // use for swapping

    for (int i = 1; i < size; i++)
    {
        printf("PASS %d ...\n ", i);
        done = true;
        for (int j = 0; j < size - i; j++)
        {
            if (a[j] > a[j + 1])
            {
                print(a, size); // for tracing
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                done = false;  // swap detected, one more pass
                printf("=> "); // for tracing
                print(a, size);
                printf("\n");
            }
        }
        if (done)
            break;
    }
}

// Print the contents of the given array of size
void print(const int a[], int size)
{
    printf("{");
    for (int i = 0; i <= size - 1; ++i)
    {
        printf("%d", a[i]);
        if (i < size - 1)
            printf(",");
    }
    printf("} ");
}

int main()
{
    const int SIZE = 9;
    int a[] = {56, 24, 93, 17, 77, 31, 44, 55, 20};

    print(a, SIZE);
    printf("\n");
    bubbleSort(a, SIZE);
    print(a, SIZE);
    printf("\n");
}
