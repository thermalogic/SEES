#include <stdio.h>
#include <stdlib.h>

int factorial(int n);

int main()
{
    int n=3;
    int res=factorial(n);  
    printf("the factorial %d  is %d",n,res);
	return 0;
}
