/*
 Parallelizing merge sort
*/
#include <iostream>
#include <thread>
#include <ctime>
#include <atomic>
#include <string>
#include <cstring>
#include<algorithm>
using namespace std;

atomic<int> CPU(8); //Maximum number of threads

void Merge(int a[], int l, int mid,int r, int b[])
{
    int p = l, p1 = l, p2 = mid + 1;
    while (p1 <= mid && p2 <= r)
        b[p++] = a[p1] < a[p2] ? a[p1++] : a[p2++];
    while (p1 <= mid)
        b[p++] = a[p1++];
    while (p2 <= r)
        b[p++] = a[p2++];
    for (int i = l; i <= r; i++)
        a[i] = b[i];
}

void MergeSort(int a[], int l, int r, int b[])
{
    if (l >= r)
        return;
    int mid = (l + r) / 2;
    MergeSort(a, l, mid, b);
    MergeSort(a, mid + 1, r, b);
    Merge(a, l,mid,r, b);
}

void Merge_Sort(int a[], int size)
{
    int *b;
    b = (int *)malloc(sizeof(int) * size);
    MergeSort(a, 0, size - 1, b);
    CPU--;
    free(b);
}

void ParallelMergeSort(int a[], int l, int r, int b[])
{
    int minparallelsize =1000;
    //int minparallelsize =10;
    if (l >= r)
        return;

    int mid = (l + r) / 2;

    thread LeftThread;
    thread RightThread;

    if (CPU > 0 && (r-l)>minparallelsize )
    {
        //cout <<"Left Thread "<<CPU <<endl;
        CPU--;
        LeftThread = thread(ParallelMergeSort, a, l, mid, b);
    }
    else
    {
        //cout <<"Left "<<CPU <<endl;
        MergeSort(a, l, mid, b);
    }   
   
    if (CPU > 0 &&(r-l)>minparallelsize)
    {
        //cout <<"Right Thread "<<CPU <<endl;
        CPU--;
        RightThread = thread(ParallelMergeSort, a, mid + 1, r, b);
    }
    else
    {
        //cout <<"Right "<<CPU <<endl;
        MergeSort(a, mid + 1, r, b);
    }   
    if (LeftThread.joinable())
        LeftThread.join();
    if (RightThread.joinable())
        RightThread.join();
    Merge(a, l, mid,r, b);
    CPU++;
    //cout <<"After Merge "<<CPU <<endl;
}

void ParallelMerge_Sort(int a[], int size)
{
    int *b;
    b = (int *)malloc(sizeof(int) * size);
    ParallelMergeSort(a, 0, size - 1, b);
    free(b);
}

void sortingtimes(string sortname, void (*f)(int *a, int size), int *a, int size)
{
    clock_t StartTime, EndTime;
    StartTime = clock();
    f(a, size);
    EndTime = clock();
    cout << "The "<<sortname<<" run times: " << (double)(EndTime - StartTime) << endl;
    cout <<"\t";
    for (int i = 0; i <20; i++)
        cout << a[i] << " ";
    cout << endl;
}


int main()
{
    const int size = 10000000;//1e7 
    int *v;
    int *a;
    v = (int *)malloc(sizeof(int) * size);
    a = (int *)malloc(sizeof(int) * size);
 
    cout <<"SIZE "<<size<<endl;
    srand((unsigned)time(NULL));
    for (int i = 0; i < size; i++)
        v[i] = (int)rand() % size+i;

    cout <<"\t";
    for (int i = 0; i < 20; i++)
        cout << v[i] << " ";
    cout << endl;

    // Merge Sort
    memcpy(a, v, sizeof(int) * size);
    sortingtimes("Merge Sort",Merge_Sort,a,size);

    // Parallel Merge Sort
    memcpy(a, v, sizeof(int) * size);
    sortingtimes("Parallel Merge Sort",ParallelMerge_Sort,a,size);
    
    // std::sort
    memcpy(a, v, sizeof(int) * size);
    clock_t StartTime, EndTime;
    StartTime = clock();
    sort(a,a+size);
    EndTime = clock();
    cout << "The std::sort run times: " << (double)(EndTime - StartTime) << endl;
    cout <<"\t";
    for(int i=0;i<20;i++)
        cout<<a[i]<<" ";
    free(a);
    free(v);
}
