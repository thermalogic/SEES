/*
gcc -o ./bin/gaussApp ./src/gaussApp.c  ./src/gauss.c ./src/gauss_am_pivoting.c -I./include 

Example :
    
    周建华，陈建龙，张小向编：《几何于代数》 科学出版社，2012
    1.4 线性方程组的求解  P29-30  例1.21
*/

#include<stdio.h>
#include<stdlib.h> 
#include "eqlinear.h" 

int main()
{   
    int i,j;
    int nrows=3;
    double x[3];
    double a[3][3]={{1.0,3.0,2.0},
                   {2.0,1.0,1.0},
                   {-1.0,2.0,3.0}};
    double b[3]={-1.0,3.0,4.0};
    
    // **ptr
    double **ptr;
    ptr=(double**)malloc(sizeof(double)*nrows);  
    for(i=0;i<nrows;i++)  
    {   ptr[i]=(double*)malloc(sizeof(double)*(nrows+1)); // +1 Augmented matrix
        for(j=0;j<nrows;j++) 
            ptr[i][j]=a[i][j];
        ptr[i][nrows]=b[i];                       
    }
                               
    gauss_am_pivoting(nrows,ptr,x);
    //gauss(nrows,ptr,b,x);
    printf("\nThe solution is: ");
    for(int i=0; i<nrows; i++)
    {
        printf("\n\tx%d=%f\t",i,x[i]); /* x1, x2, x3 are the required solutions*/
    }
    // **ptr                   
    for(i=0;i<nrows;i++)  
       free(ptr[i]);
    free(ptr); 
 
    return(0);
}
