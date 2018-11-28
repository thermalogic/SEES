
from ctypes import cdll,c_int,c_double,POINTER

_lib = cdll.LoadLibrary('./demo/bin/libmultifuns.dll')

# double dprod(double *x, int n)
def dprod(x):
    _lib.dprod.argtypes = [POINTER(c_double), c_int]
    _lib.dprod.restype  = c_double
    n = len(x)
    #  convert a Python list into a C array by using ctypes
    arr= (c_double * n)(*x)
    return _lib.dprod(arr,int(n))

# int isum(int array[], int size);
def isum(x):
    _lib.sum.argtypes = [POINTER(c_int), c_int]
    _lib.sum.restype =c_int
    n = len(x)
    #  convert a Python list into a C array by using ctypes
    arr= (c_int * n)(*x)
    return _lib.sum(arr,int(n))
