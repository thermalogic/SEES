#include <stdio.h>
#include <stdlib.h>

int GetNumber(int *v);

int main()
{
    int v=10;
    int res=GetNumber(&v); // &v: the  address of the v 
    printf("%d %d",v,res);
	return 0;
}
