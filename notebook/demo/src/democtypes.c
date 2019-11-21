
// 1 Struct
typedef struct
{
    int nNo;
    float fValue;
} SimpleStruct;

__declspec(dllexport)  void __stdcall  TestSimpleStruct(SimpleStruct v,SimpleStruct *res)
{
  res->fValue= v.fValue+2;
  res->nNo=v.nNo+2;
  // return res->nNo;
}

// 2 one-dimensional array :
//    return: *narray: ith ,item =i
__declspec(dllexport)  void  __stdcall  TestArray1(double *narray,int size)
{
  for(int i=0; i<size; i++)
  {
     narray[i]=i;  
  }
}

// 3  two-dimensional array : double **ptr
//       return:  2*item
__declspec(dllexport)  void  __stdcall  TestArray22(double **ptr,int row, int col)
{
    int i, j;
    for(i=0; i<row; i++)
    {
        for(j=0; j<col; j++)
        {
            ptr[i][j]=2*ptr[i][j];
        }
	} 
}
