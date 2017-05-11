
from ctypes import cdll,c_void_p,c_int,c_long,c_double,POINTER,byref
import numpy as np

_lib = cdll.LoadLibrary('./code/gcc/libmultifuns.dll')
#_lib = np.ctypeslib.load_library('libmultifuns', '.')

_lib.hello.argtypes = []
_lib.hello.restype  =  c_void_p

_lib.dprod.argtypes = [np.ctypeslib.ndpointer(dtype=np.float), c_int]
_lib.dprod.restype  = c_double

_lib.LinearFibonacci.argtypes = [c_int]
_lib.LinearFibonacci.restype= c_long

def hello():
    return _lib.hello()

def dprod(x):
    n = len(x)
    x = np.asarray(x, dtype=np.float)
    return _lib.dprod(x, int(n))

def LinearFibonacci(n):
    return _lib.LinearFibonacci(int(n))

#unsigned long fibonacci(int n, unsigned long *fib_cache);
def fibonacci(n):
    fibcache = (POINTER(c_long)*n)()
    fib=c_long()
    fib=_lib.LinearFibonacci(int(n),byref(fibcache))
    return  fib