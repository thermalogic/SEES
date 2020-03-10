
int factorial(int n);

//__declspec(dllexport) int __stdcall  factorial(int n); 

int factorial(int n)
{
    if (n == 0 ) {
        return 1;
    }
    else 
    {
        return n * factorial(n - 1);
    }
}
