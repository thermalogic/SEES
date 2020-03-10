
int GetNumber(int *v); 

//__declspec(dllexport) int __stdcall  GetNumber(int *v); 

int GetNumber(int *v)
{
    int temp;
	temp=*v+1;
	*v=temp;
	return (*v)+1;
}
