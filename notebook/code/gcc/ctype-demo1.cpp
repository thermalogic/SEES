
// 1 Struct
struct SimpleStruct
{
    int nNo;
    float fValue;
};

extern "C" __declspec(dllexport) int __stdcall TestSimpleStruct(int *n, int &m, SimpleStruct struin, SimpleStruct *struout)
{
    struout->fValue = struin.fValue + 2;
    struout->nNo = struin.nNo + 3;

    *n = struin.nNo + 20;
    m = *n + 30;
    return struout->nNo;
}

// 2 using the name of one-dimensional array in Python.non byref
extern "C" __declspec(dllexport) void __stdcall TestArray1(int nsize, double *narray)
{
    for (int i = 0; i < nsize; i++)
    {
        narray[i] = i * 2.3;
    }
}

// 3 using the name of two-dimensional array in Python.  non byref
extern "C" __declspec(dllexport) void __stdcall TestArray21(int ni, int nj, double *ptr)
{
    int i, j;
    for (i = 0; i < ni; i++)
    {
        for (j = 0; j < nj; j++)
        {
            ptr[i * ni + j] = ptr[i * ni + j] + i * ni + j;
        }
    }
}

// 4 using byref in Python
extern "C" __declspec(dllexport) void __stdcall TestArray22(int ni, int nj, double **ptr)
{
    int i, j;
    for (i = 0; i < ni; i++)
    {
        for (j = 0; j < nj; j++)
        {
            ptr[i][j] = ptr[i][j] + i * ni + j;
        }
    }
}
